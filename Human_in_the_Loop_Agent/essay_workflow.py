
import os
import sqlite3
import uuid
from pathlib import Path
from typing import TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "essay_checkpoints.sqlite"
MODEL_NAME = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
MAX_REVISIONS = 2

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is missing from .env.")

if not os.getenv("TAVILY_API_KEY"):
    raise ValueError("TAVILY_API_KEY is missing from .env.")


# Application state shared by all graph nodes.
class EssayState(TypedDict):
    topic: str
    research: str
    draft: str
    review_feedback: str
    revision_count: int
    approved: bool
    status: str


model = ChatGroq(model=MODEL_NAME, temperature=0)

search_tool = TavilySearch(
    max_results=3,
    topic="general",
    search_depth="basic",
)


# Node 1: research the topic using Tavily.
def research_topic(state: EssayState):
    results = search_tool.invoke(
        {"query": f"Reliable sources and key facts about: {state['topic']}"}
    )

    research_items = []

    if isinstance(results, dict):
        for item in results.get("results", []):
            title = item.get("title", "Untitled source")
            url = item.get("url", "")
            content = item.get("content", "")

            research_items.append(
                f"Source: {title}\nURL: {url}\n"
                f"Information: {content[:1500]}"
            )

    research = "\n\n".join(research_items)

    if not research:
        research = str(results)[:4500]

    print("Research completed.")

    return {"research": research}


# Node 2: create the first essay draft.
def write_essay(state: EssayState):
    response = model.invoke(
        [
            SystemMessage(
                content=(
                    "You are an essay-writing assistant. "
                    "Write a clear, well-organized essay of approximately "
                    "300 words using the supplied research. Include an "
                    "introduction, main body, and conclusion. Do not invent "
                    "sources. Cite available sources with their URLs in "
                    "Markdown links. If the research is insufficient, "
                    "be transparent about its limitations."
                )
            ),
            HumanMessage(
                content=(
                    f"Essay topic: {state['topic']}\n\n"
                    f"Research:\n{state['research']}\n\n"
                    "Write the essay draft."
                )
            ),
        ]
    )

    return {
        "draft": str(response.content),
        "status": "awaiting_review",
        "approved": False,
    }


# Node 3: pause until a human approves or requests a revision.
def human_review(state: EssayState):
    decision = interrupt(
        {
            "type": "essay_review",
            "topic": state["topic"],
            "draft": state["draft"],
            "revision_count": state["revision_count"],
            "max_revisions": MAX_REVISIONS,
            "message": (
                "Review the draft. Choose approve or revise, "
                "and provide feedback if needed."
            ),
        }
    )

    action = decision.get("action", "revise")
    feedback = decision.get("feedback", "").strip()

    if action == "approve":
        return {
            "approved": True,
            "status": "approved",
            "review_feedback": feedback,
        }

    if state["revision_count"] >= MAX_REVISIONS:
        return {
            "approved": False,
            "status": "revision_limit_reached",
            "review_feedback": feedback,
        }

    return {
        "approved": False,
        "status": "revision_requested",
        "review_feedback": feedback or "Improve clarity and organization.",
    }


# Node 4: revise the draft based on human feedback.
def revise_essay(state: EssayState):
    response = model.invoke(
        [
            SystemMessage(
                content=(
                    "Revise an essay using the reviewer feedback. "
                    "Preserve accurate information and source links. "
                    "Return the revised essay only."
                )
            ),
            HumanMessage(
                content=(
                    f"Topic: {state['topic']}\n\n"
                    f"Research:\n{state['research']}\n\n"
                    f"Previous draft:\n{state['draft']}\n\n"
                    f"Reviewer feedback:\n{state['review_feedback']}\n\n"
                    "Produce the revised essay."
                )
            ),
        ]
    )

    print("Revision completed.")

    return {
        "draft": str(response.content),
        "revision_count": state["revision_count"] + 1,
        "status": "awaiting_review",
    }


# Decide whether to finish or revise.
def route_after_review(state: EssayState):
    if state["approved"]:
        return "finish"

    if state["revision_count"] >= MAX_REVISIONS:
        return "finish"

    return "revise"


def build_graph(checkpointer):
    builder = StateGraph(EssayState)

    builder.add_node("research", research_topic)
    builder.add_node("write", write_essay)
    builder.add_node("human_review", human_review)
    builder.add_node("revise", revise_essay)

    builder.add_edge(START, "research")
    builder.add_edge("research", "write")
    builder.add_edge("write", "human_review")

    builder.add_conditional_edges(
        "human_review",
        route_after_review,
        {
            "revise": "revise",
            "finish": END,
        },
    )

    builder.add_edge("revise", "human_review")

    return builder.compile(checkpointer=checkpointer)


def open_graph():
    connection = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    checkpointer = SqliteSaver(connection)
    checkpointer.setup()

    return build_graph(checkpointer), connection


def run_cli():
    graph, connection = open_graph()
    thread_id = f"essay-{uuid.uuid4().hex[:8]}"
    config = {"configurable": {"thread_id": thread_id}}

    try:
        topic = input("Enter your essay topic: ").strip()

        if not topic:
            print("Please enter a topic.")
            return

        graph.invoke(
            {
                "topic": topic,
                "research": "",
                "draft": "",
                "review_feedback": "",
                "revision_count": 0,
                "approved": False,
                "status": "started",
            },
            config=config,
        )

        while True:
            current_state = graph.get_state(config)
            values = current_state.values

            print("\n" + "=" * 60)
            print("ESSAY DRAFT")
            print("=" * 60)
            print(values.get("draft", ""))

            if not current_state.next:
                print(f"\nWorkflow finished: {values.get('status')}")
                break

            action = input(
                "\nApprove (a) or request a revision (r)? "
            ).strip().lower()

            if action in ("a", "approve"):
                decision = {"action": "approve", "feedback": ""}
            elif action in ("r", "revise"):
                feedback = input("What should be improved? ").strip()
                decision = {"action": "revise", "feedback": feedback}
            else:
                print("Please enter 'a' to approve or 'r' to revise.")
                continue

            graph.invoke(Command(resume=decision), config=config)

        final_state = graph.get_state(config).values
        print("\nFinal status:", final_state.get("status"))
        print("Revisions:", final_state.get("revision_count"))

    finally:
        connection.close()


if __name__ == "__main__":
    run_cli()
