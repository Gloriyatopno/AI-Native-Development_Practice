
import ast
import operator
import os
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

if not API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Add it to the local .env file."
    )

client = Groq(api_key=API_KEY)


# Tool 1: Look up mocked average dog weights.
DOG_WEIGHTS = {
    "toy poodle": 7,
    "border collie": 37,
    "scottish terrier": 20,
}


def average_dog_weight(breed):
    """Return the mock average weight for a supported dog breed."""
    breed = " ".join(breed.strip().lower().split())
    breed = breed.strip(" .?!")

    if breed not in DOG_WEIGHTS:
        available = ", ".join(DOG_WEIGHTS.keys())
        return f"Unknown breed. Available breeds: {available}."

    weight = DOG_WEIGHTS[breed]
    return f"The average weight of a {breed.title()} is {weight} pounds."


# Tool 2: Evaluate arithmetic without using unrestricted eval().
def _calculate_node(node):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    if isinstance(node, ast.Expression):
        return _calculate_node(node.body)

    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
        left = _calculate_node(node.left)
        right = _calculate_node(node.right)
        return allowed_operators[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in (
        ast.UAdd,
        ast.USub,
    ):
        value = _calculate_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    raise ValueError("Only basic arithmetic is allowed.")


def calculate(expression):
    """Calculate an arithmetic expression containing numbers and operators."""
    if len(expression) > 100:
        return "Calculation input is too long."

    try:
        tree = ast.parse(expression, mode="eval")
        result = _calculate_node(tree)
        return f"The result of {expression} is {result:g}."
    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError):
        return "Could not calculate that expression. Use basic arithmetic only."


# The LLM uses these exact tool names when requesting an action.
TOOLS = {
    "average_dog_weight": average_dog_weight,
    "calculate": calculate,
}


SYSTEM_PROMPT = """
You are a simple ReAct agent.

Available tools:
1. average_dog_weight: Input is a supported dog breed.
2. calculate: Input is a basic arithmetic expression.

Supported dog breeds:
- toy poodle: 7 pounds
- border collie: 37 pounds
- scottish terrier: 20 pounds

Follow this exact format.

When a tool is needed, return:
Thought: Briefly state the next step.
Action: tool_name: tool input
Pause

When the task is complete, return:
Answer: Your final answer.

Rules:
- Use only the tools listed above.
- Request one tool action at a time.
- Use observations returned by tools to decide the next step.
- Do not invent tool results.
- If a tool reports an error, explain the limitation or try a suitable correction.
- If a question is unrelated to the tools and can be answered directly,
  answer it without calling a tool.
- Keep responses concise.
"""


class Agent:
    def __init__(self, system_message=SYSTEM_PROMPT):
        self.messages = [
            {"role": "system", "content": system_message}
        ]

    def __call__(self, message):
        # Add the user's question or the latest tool observation.
        self.messages.append({"role": "user", "content": message})

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=self.messages,
            temperature=0.7,
            max_tokens=300,
            reasoning_effort="none",
            )

        assistant_message = response.choices[0].message.content or ""
        self.messages.append(
            {"role": "assistant", "content": assistant_message}
        )

        return assistant_message


# Identify an action requested by the LLM.
ACTION_PATTERN = re.compile(
    r"(?im)^\s*Action\s*:\s*([a-zA-Z_]\w*)\s*:\s*(.+?)\s*$"
)

ANSWER_PATTERN = re.compile(
    r"(?im)^\s*Answer\s*:\s*(.+(?:\n(?!\s*(?:Thought|Action|Pause):?).+)*)"
)


def query(question, max_turns=8):
    """Run the agent until it answers or reaches the turn limit."""
    agent = Agent()
    next_message = question

    for turn in range(1, max_turns + 1):
        response = agent(next_message)

        print(f"\n--- Agent turn {turn} ---")
        print(response)

        # If the LLM requested a tool, execute it.
        action_match = ACTION_PATTERN.search(response)

        if action_match:
            tool_name = action_match.group(1).strip()
            tool_input = action_match.group(2).strip()

            if tool_name not in TOOLS:
                print(f"Unknown action requested: {tool_name}")
                return "The agent requested an unknown tool."

            print(f"\nRunning tool: {tool_name}")
            print(f"Tool input: {tool_input}")

            try:
                observation = TOOLS[tool_name](tool_input)
            except Exception as error:
                observation = f"Tool error: {error}"

            print(f"Observation: {observation}")

            # Return the observation to the LLM for the next turn.
            next_message = (
                f"Observation: {observation}\n"
                "Use this result to continue the task. "
                "Call another tool if needed, or give the final answer."
            )
            continue

        # If the LLM has finished, return its final answer.
        answer_match = ANSWER_PATTERN.search(response)

        if answer_match:
            return answer_match.group(1).strip()

        print("The agent did not return a recognized action or answer.")
        return response

    return f"The agent stopped after reaching the limit of {max_turns} turns."


if __name__ == "__main__":
    question = input("Enter your question: ").strip()

    if not question:
        print("Please enter a question.")
    else:
        final_answer = query(question)
        print("\n=== Final Answer ===")
        print(final_answer)
