import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.0
)


# ============================================================
# TEST DATA
# ============================================================

examples = [
    {
        "query": "What is 2 + 2?",
        "answer": "4"
    },
    {
        "query": "What planet is known as the Red Planet?",
        "answer": "Mars"
    },
    {
        "query": "What is the capital of France?",
        "answer": "Paris"
    }
]


# These simulate answers produced by an application.
predictions = [
    {
        "query": "What is 2 + 2?",
        "result": "The answer is 4."
    },
    {
        "query": "What planet is known as the Red Planet?",
        "result": "Mars is known as the Red Planet."
    },
    {
        "query": "What is the capital of France?",
        "result": "The capital of France is Berlin."
    }
]


# ============================================================
# MANUAL EVALUATION
# ============================================================

print("\n" + "=" * 60)
print("1. MANUAL EVALUATION")
print("=" * 60)

for i, example in enumerate(examples):
    print(f"\nExample {i + 1}")
    print("Question:", example["query"])
    print("Expected:", example["answer"])
    print("Predicted:", predictions[i]["result"])


# ============================================================
# LLM-ASSISTED EVALUATION
# ============================================================

print("\n" + "=" * 60)
print("2. LLM-ASSISTED EVALUATION")
print("=" * 60)

evaluation_prompt = """
You are evaluating an LLM answer.

Compare the expected answer with the predicted answer.

Return exactly:
GRADE: PASS
or
GRADE: FAIL

Then give one short reason.

Question:
{question}

Expected answer:
{expected}

Predicted answer:
{predicted}

Judge based on meaning, not exact wording.
"""

passed = 0

for i, example in enumerate(examples):

    prompt = evaluation_prompt.format(
        question=example["query"],
        expected=example["answer"],
        predicted=predictions[i]["result"]
    )

    response = llm.invoke(prompt).content

    print(f"\nExample {i + 1}")
    print("Question:", example["query"])
    print("Expected:", example["answer"])
    print("Predicted:", predictions[i]["result"])
    print("Evaluation:", response)

    if "GRADE: PASS" in response.upper():
        passed += 1


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("3. EVALUATION SUMMARY")
print("=" * 60)

print(f"Total examples: {len(examples)}")
print(f"Passed: {passed}")
print(f"Failed: {len(examples) - passed}")

if examples:
    accuracy = (passed / len(examples)) * 100
    print(f"Evaluation score: {accuracy:.0f}%")