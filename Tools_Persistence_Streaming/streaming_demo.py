
import asyncio

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from agent_workflow import (
    AgentState,
    DB_PATH,
    SYSTEM_PROMPT,
    content_to_text,
    llm_with_tools,
    tools,
)


# Async LLM node: stream the model response in chunks.
async def call_llm_streaming(state: AgentState):
    messages_for_model = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    response = None

    async for chunk in llm_with_tools.astream(messages_for_model):
        response = chunk if response is None else response + chunk

    if response is None:
        raise RuntimeError("The LLM did not return a response.")

    return {"messages": [response]}


def build_streaming_graph(checkpointer):
    builder = StateGraph(AgentState)

    builder.add_node("llm", call_llm_streaming)
    builder.add_node("tools", ToolNode(tools))

    builder.add_conditional_edges(
        "llm",
        tools_condition,
        {
            "tools": "tools",
            END: END,
        },
    )

    builder.add_edge("tools", "llm")
    builder.set_entry_point("llm")

    return builder.compile(checkpointer=checkpointer)


async def main():
    question = input("Enter your question: ").strip()

    if not question:
        print("Please enter a question.")
        return

    # Use a separate thread for this streaming demonstration.
    config = {
        "configurable": {
            "thread_id": "token-stream-demo",
        }
    }

    async with AsyncSqliteSaver.from_conn_string(DB_PATH) as checkpointer:
        graph = build_streaming_graph(checkpointer)

        print("\n--- Streaming Workflow ---")

        async for event in graph.astream_events(
            {"messages": [HumanMessage(content=question)]},
            config=config,
            version="v2",
        ):
            event_type = event.get("event")
            event_data = event.get("data", {})

            if event_type == "on_tool_start":
                print(
                    f"\n[Tool started: {event.get('name')}] "
                    f"{event_data.get('input', '')}"
                )

            elif event_type == "on_tool_end":
                output = event_data.get("output")
                print(f"[Tool finished: {event.get('name')}]")
                if output is not None:
                    text = content_to_text(
                        getattr(output, "content", output)
                    )
                    print(text[:500])

            elif event_type == "on_chat_model_stream":
                chunk = event_data.get("chunk")
                content = getattr(chunk, "content", "")

                if isinstance(content, str) and content:
                    print(content, end="", flush=True)

                elif isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict):
                            text = block.get("text", "")
                            if text:
                                print(text, end="", flush=True)

        print("\n\nStreaming completed.")


if __name__ == "__main__":
    asyncio.run(main())
