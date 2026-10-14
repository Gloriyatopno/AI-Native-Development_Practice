
import ast
import operator
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
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

load_dotenv()

MODEL_NAME = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is missing from the .env file.")


# 1. Define the application state.
class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]


# 2. Define the tools.

DOG_WEIGHTS = {
    "toy poodle": 7,
    "border collie": 37,
    "scottish terrier": 20,
}


@tool
def average_dog_weight(breed: str) -> str:
    """Look up the mock average weight in pounds for a supported dog breed."""
    breed = " ".join(breed.lower().strip().split()).strip(" .?!")

    if breed not in DOG_WEIGHTS:
        available = ", ".join(DOG_WEIGHTS)
        return f"Breed not found. Supported breeds: {available}."

    weight = DOG_WEIGHTS[breed]
    return f"The average weight of a {breed.title()} is {weight} pounds."


def evaluate_expression(node):
    """Evaluate only basic arithmetic syntax."""
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    if isinstance(node, ast.Expression):
        return evaluate_expression(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
        left = evaluate_expression(node.left)
        right = evaluate_expression(node.right)
        return allowed_operators[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in (ast.UAdd, ast.USub):
        value = evaluate_expression(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    raise ValueError("Only basic arithmetic is supported.")


@tool
def calculate(expression: str) -> str:
    """Calculate an arithmetic expression using basic mathematical operators."""
    if len(expression) > 100:
        return "Calculation input is too long."

    try:
        tree = ast.parse(expression, mode="eval")
        result = evaluate_expression(tree)
        return f"The result of {expression} is {result:g}."
    except (
        SyntaxError,
        ValueError,
        TypeError,
        ZeroDivisionError,
        OverflowError,
    ):
        return "Could not calculate the expression. Use basic arithmetic only."


tools = [average_dog_weight, calculate]


# 3. Initialize the LLM and make the tools available to it.
llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0,
)

llm_with_tools = llm.bind_tools(tools)


SYSTEM_PROMPT = """
You are a helpful assistant using a small set of tools.

Use average_dog_weight when you need a supported dog's mock average weight.
Use calculate when you need arithmetic.
Use tool results rather than inventing values.
When the task is complete, provide a clear, concise answer.
For unrelated questions, answer directly without calling a tool.

Supported dog weights:
- Toy Poodle: 7 pounds
- Border Collie: 37 pounds
- Scottish Terrier: 20 pounds
"""


# 4. Define the LLM node.
def call_llm(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


# 5. Build the graph and connect its nodes.
builder = StateGraph(AgentState)

builder.add_node("llm", call_llm)
builder.add_node("tools", ToolNode(tools))

# Choose the next step based on whether the LLM requested a tool.
builder.add_conditional_edges(
    "llm",
    tools_condition,
    {
        "tools": "tools",
        END: END,
    },
)

# After tool execution, return to the LLM with the tool results.
builder.add_edge("tools", "llm")

builder.set_entry_point("llm")

# Compile the graph so it can be invoked.
graph = builder.compile()


# 6. Run the workflow and inspect its state.
def run_agent(question: str):
    initial_state = {
        "messages": [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=question),
        ]
    }

    result = graph.invoke(initial_state)

    print("\n--- LangGraph Workflow ---")

    for message in result["messages"]:
        if isinstance(message, AIMessage) and message.tool_calls:
            for tool_call in message.tool_calls:
                print(
                    f"Tool requested: {tool_call['name']} "
                    f"with input {tool_call['args']}"
                )

        elif isinstance(message, ToolMessage):
            print(f"Tool observation ({message.name}): {message.content}")

    final_message = result["messages"][-1]

    print("\n--- Final Answer ---")
    print(final_message.content)

    print("\n--- State Summary ---")
    print(f"Total messages in final state: {len(result['messages'])}")
    print("Graph execution completed.")


if __name__ == "__main__":
    question = input("Enter your question: ").strip()

    if question:
        run_agent(question)
    else:
        print("Please enter a question.")
