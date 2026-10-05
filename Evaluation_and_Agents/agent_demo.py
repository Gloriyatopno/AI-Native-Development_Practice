import os
from datetime import date

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

MODEL_NAME = "openai/gpt-oss-20b"


# ============================================================
# 1. DEFINE CUSTOM TOOLS
# ============================================================

@tool
def calculate_percentage(number: float, percentage: float) -> str:
    """Calculate a percentage of a number.

    Use this tool for percentage calculation questions.
    """
    result = number * (percentage / 100)
    return str(result)


@tool
def get_today_date() -> str:
    """Return today's date.

    Use this tool for questions asking for today's date.
    This tool does not require any input.
    """
    return str(date.today())


tools = [
    calculate_percentage,
    get_today_date,
]


# ============================================================
# 2. CREATE AGENT
# ============================================================

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.0,
)

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the available tools when they are appropriate. "
        "Answer clearly and briefly."
    ),
)


# ============================================================
# 3. TEST TOOL SELECTION
# ============================================================

def run_agent(question):
    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    messages = result["messages"]

    tool_calls = []

    for message in messages:
        if hasattr(message, "tool_calls") and message.tool_calls:
            tool_calls.extend(message.tool_calls)

    final_answer = messages[-1].content

    return tool_calls, final_answer


print("\n" + "=" * 60)
print("1. PERCENTAGE TOOL TEST")
print("=" * 60)

question = "What is 25% of 300?"

tool_calls, answer = run_agent(question)

print("Question:", question)
print("\nTool selected:")

if tool_calls:
    for call in tool_calls:
        print("-", call["name"])
        print("  Arguments:", call["args"])
else:
    print("No tool call detected.")

print("\nFinal answer:")
print(answer)


print("\n" + "=" * 60)
print("2. DATE TOOL TEST")
print("=" * 60)

question = "What is today's date?"

tool_calls, answer = run_agent(question)

print("Question:", question)
print("\nTool selected:")

if tool_calls:
    for call in tool_calls:
        print("-", call["name"])
        print("  Arguments:", call["args"])
else:
    print("No tool call detected.")

print("\nFinal answer:")
print(answer)


print("\n" + "=" * 60)
print("3. AGENT DECISION-MAKING")
print("=" * 60)

print(
    "The agent receives the question, decides whether a tool is needed, "
    "selects the appropriate tool, receives the tool result, and then "
    "produces the final answer."
)