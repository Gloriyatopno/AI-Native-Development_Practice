
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver

from agent_workflow import DB_PATH, build_graph, content_to_text


THREAD_ID = "persistence-demo"


def ask_question(graph, question):
    config = {
        "configurable": {
            "thread_id": THREAD_ID,
        }
    }

    result = graph.invoke(
        {"messages": [HumanMessage(content=question)]},
        config=config,
    )

    answer = content_to_text(result["messages"][-1].content)

    print(f"\nQuestion: {question}")
    print(f"Answer: {answer}")

    return result


if __name__ == "__main__":
    # File-backed SQLite keeps checkpoints between program runs.
    with SqliteSaver.from_conn_string(DB_PATH) as checkpointer:
        graph = build_graph(checkpointer)

        print(f"Conversation thread: {THREAD_ID}")

        # First interaction
        ask_question(
            graph,
            "Search for the official LangGraph documentation and "
            "explain what LangGraph does in one sentence.",
        )

        # Follow-up: reuses the same thread and saved message history.
        ask_question(
            graph,
            "Based on our previous exchange, what did I ask you to explain?",
        )

        config = {
            "configurable": {
                "thread_id": THREAD_ID,
            }
        }

        saved_state = graph.get_state(config)
        saved_messages = saved_state.values.get("messages", [])

        print("\n--- Persistence Check ---")
        print(f"Messages in saved state: {len(saved_messages)}")
        print("Conversation checkpoint retrieved successfully.")
