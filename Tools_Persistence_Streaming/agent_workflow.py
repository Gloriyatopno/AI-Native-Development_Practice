
import os
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import (
    AIMessage,
    AnyMessage,
    HumanMessage,
    SystemMessage,
    ToolMessage,
)
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
DB_PATH = "agent_checkpoints.sqlite"

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env.")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing from .env.")


# Application state: preserve messages between graph steps.
class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


SYSTEM_PROMPT = """
You are a helpful web research assistant.

Use the web search tool when a question needs current information,
recent news, facts that may have changed, or supporting sources.

Use the search results as evidence. Do not invent search results,
dates, facts, or URLs. Give a concise answer and include relevant
source titles and URLs when they are available in the results.

For follow-up questions, use the existing conversation context when
appropriate. If the available evidence is insufficient, say so.
"""


# Search tool: returns structured web search results.
search_tool = TavilySearch(
    max_results=3,
    topic="general",
    search_depth="basic",
    include_answer=False,
    include_raw_content=False,
)

tools = [search_tool]

# Make the search tool available to the LLM.
llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0,
)
llm_with_tools = llm.bind_tools(tools)


# Node 1: ask the LLM to decide what to do.
def call_llm(state: AgentState):
    messages = state["messages"]

    # Supply the system instructions without duplicating them
    # in the stored conversation history.
    messages_for_model = [
        SystemMessage(content=SYSTEM_PROMPT),
        *messages,
    ]

    response = llm_with_tools.invoke(messages_for_model)
    return {"messages": [response]}


# Build the graph.
def build_graph(checkpointer):
    builder = StateGraph(AgentState)

    builder.add_node("llm", call_llm)
    builder.add_node("tools", ToolNode(tools))

    # If the model requested a tool, execute it.
    # Otherwise, finish the graph.
    builder.add_conditional_edges(
        "llm",
        tools_condition,
        {
            "tools": "tools",
            END: END,
        },
    )

    # After a search, return the result to the LLM.
    builder.add_edge("tools", "llm")

    builder.set_entry_point("llm")

    return builder.compile(checkpointer=checkpointer)


def content_to_text(content):
    """Convert common LangChain message content to readable text."""
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("text"):
                parts.append(item["text"])
            else:
                parts.append(str(item))
        return "\n".join(parts)

    return str(content)


# Stream graph updates so we can see each step as it completes.
def stream_question(graph, question, thread_id="search-demo"):
    config = {
        "configurable": {
            "thread_id": thread_id,
        }
    }

    print(f"\nConversation thread: {thread_id}")
    print(f"Question: {question}")

    for update in graph.stream(
        {"messages": [HumanMessage(content=question)]},
        config=config,
        stream_mode="updates",
    ):
        for node_name, node_update in update.items():
            print(f"\n--- Node completed: {node_name} ---")

            for message in node_update.get("messages", []):
                if isinstance(message, AIMessage):
                    if message.tool_calls:
                        for tool_call in message.tool_calls:
                            print(
                                "Tool requested:",
                                tool_call["name"],
                                tool_call["args"],
                            )
                    elif message.content:
                        print(
                            "Assistant:",
                            content_to_text(message.content),
                        )

                elif isinstance(message, ToolMessage):
                    observation = content_to_text(message.content)

                    # Keep terminal output readable.
                    if len(observation) > 900:
                        observation = observation[:900] + "... [truncated]"

                    print(f"Tool observation ({message.name}):")
                    print(observation)


if __name__ == "__main__":
    question = input("Enter a question to research: ").strip()
    thread_id = input("Conversation ID [search-demo]: ").strip()
    thread_id = thread_id or "search-demo"

    if not question:
        print("Please enter a question.")
    else:
        with SqliteSaver.from_conn_string(DB_PATH) as checkpointer:
            graph = build_graph(checkpointer)
            stream_question(graph, question, thread_id)
