import os
import json
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

MODEL = "openai/gpt-oss-20b"


def get_client():
    """Create and return the Groq client."""
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file.")

    return Groq(api_key=api_key)


def generate_response(prompt):
    """Generate an LLM response for the given prompt."""
    client = get_client()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=300
    )

    return response.choices[0].message.content.strip()


# ---------------------------------------------------------
# Part 1: Single-answer evaluation
# ---------------------------------------------------------

single_answer_tests = [
    {
        "question": "What is the capital of France?",
        "ideal_answer": "Paris"
    },
    {
        "question": "What is 5 + 7?",
        "ideal_answer": "12"
    },
    {
        "question": "What planet do humans live on?",
        "ideal_answer": "Earth"
    },
    {
        "question": "What language is commonly used for web page structure?",
        "ideal_answer": "HTML"
    },
    {
        "question": "What does CPU stand for?",
        "ideal_answer": "Central Processing Unit"
    }
]


def evaluate_single_answer(generated, ideal):
    """
    Compare a generated answer with the expected answer.

    Returns 1 for a match and 0 otherwise.
    """
    generated_clean = generated.strip().lower()
    ideal_clean = ideal.strip().lower()

    return 1 if generated_clean == ideal_clean else 0


def run_single_answer_evaluation():
    """Run evaluation where there is one expected answer."""
    print("\n" + "=" * 60)
    print("PART 1: SINGLE-ANSWER EVALUATION")
    print("=" * 60)

    total_score = 0

    for i, test in enumerate(single_answer_tests, start=1):
        generated = generate_response(
            f"Answer with only the final answer.\n\n"
            f"Question: {test['question']}"
        )

        score = evaluate_single_answer(
            generated,
            test["ideal_answer"]
        )

        total_score += score

        result = "PASS" if score == 1 else "FAIL"

        print(f"\nTest {i}")
        print(f"Question: {test['question']}")
        print(f"Expected: {test['ideal_answer']}")
        print(f"Generated: {generated}")
        print(f"Result: {result}")

    accuracy = total_score / len(single_answer_tests)

    print("\nSingle-answer accuracy:")
    print(f"{total_score}/{len(single_answer_tests)} = {accuracy:.2%}")

    return accuracy


# ---------------------------------------------------------
# Part 2: Rubric-based evaluation
# ---------------------------------------------------------

rubric_test = {
    "customer_question": (
        "What is the SmartX ProPhone price and does it support 5G?"
    ),
    "context": {
        "product": "SmartX ProPhone",
        "price": 799,
        "features": [
            "6.5-inch OLED",
            "128GB",
            "48MP camera",
            "5G"
        ]
    }
}


def evaluate_with_rubric(test, assistant_answer):
    """
    Evaluate an open-ended answer using a simple rubric.

    The evaluator checks:
    1. Whether the answer uses only the supplied context.
    2. Whether it answers the questions asked.
    3. Whether it contains information that conflicts with the context.
    """

    prompt = f"""
You are evaluating an assistant response.

Customer question:
{test['customer_question']}

Available product context:
{json.dumps(test['context'], indent=2)}

Assistant response:
{assistant_answer}

Evaluate the response using these criteria:

1. Based only on the provided context: Y or N
2. Contains unsupported information: Y or N
3. Conflicts with the provided context: Y or N
4. Answers the customer's question completely: Y or N

Return ONLY valid JSON in this format:

{{
    "based_on_context": "Y",
    "unsupported_information": "N",
    "conflicts_with_context": "N",
    "answers_question": "Y"
}}
"""

    result = generate_response(prompt)

    try:
        return json.loads(result)
    except json.JSONDecodeError:
        return {
            "based_on_context": "N",
            "unsupported_information": "Y",
            "conflicts_with_context": "Y",
            "answers_question": "N"
        }


def run_rubric_evaluation():
    """Run a no-single-right-answer evaluation."""

    print("\n" + "=" * 60)
    print("PART 2: RUBRIC-BASED EVALUATION")
    print("=" * 60)

    assistant_answer = (
        "The SmartX ProPhone costs $799 and supports 5G."
    )

    evaluation = evaluate_with_rubric(
        rubric_test,
        assistant_answer
    )

    print("\nCustomer question:")
    print(rubric_test["customer_question"])

    print("\nAssistant response:")
    print(assistant_answer)

    print("\nRubric evaluation:")
    print(json.dumps(evaluation, indent=2))

    return evaluation


# ---------------------------------------------------------
# Part 3: Expert-answer comparison
# ---------------------------------------------------------

expert_test = {
    "question": (
        "Which product is more highly rated: "
        "SmartX ProPhone or FotoSnap DSLR Camera?"
    ),
    "context": {
        "SmartX ProPhone": {
            "rating": 4.5
        },
        "FotoSnap DSLR Camera": {
            "rating": 4.7
        }
    },
    "ideal_answer": (
        "The FotoSnap DSLR Camera is more highly rated, "
        "with a rating of 4.7 compared with 4.5 for the "
        "SmartX ProPhone."
    )
}


def evaluate_vs_expert(test, assistant_answer):
    """
    Compare an open-ended response with an expert answer.

    The evaluator focuses on factual consistency rather
    than requiring identical wording.
    """

    prompt = f"""
You are evaluating an assistant response against an expert answer.

Question:
{test['question']}

Available context:
{json.dumps(test['context'], indent=2)}

Expert answer:
{test['ideal_answer']}

Assistant answer:
{assistant_answer}

Classify the assistant answer using exactly one category:

A = Correct and fully supported by the context
B = Correct but includes extra information that is still supported
C = Partially correct or incomplete
D = Contains a factual disagreement with the context
E = Different wording but still factually equivalent

Return ONLY the letter A, B, C, D, or E.
"""

    result = generate_response(prompt)

    return result.strip().upper()


def run_expert_evaluation():
    """Run expert-answer comparison."""

    print("\n" + "=" * 60)
    print("PART 3: EXPERT-ANSWER COMPARISON")
    print("=" * 60)

    assistant_answer = (
        "The FotoSnap DSLR Camera has the higher rating at 4.7, "
        "while the SmartX ProPhone has a rating of 4.5."
    )

    result = evaluate_vs_expert(
        expert_test,
        assistant_answer
    )

    print("\nQuestion:")
    print(expert_test["question"])

    print("\nExpert answer:")
    print(expert_test["ideal_answer"])

    print("\nAssistant answer:")
    print(assistant_answer)

    print(f"\nEvaluation category: {result}")

    return result


# ---------------------------------------------------------
# Part 4: Final evaluation report
# ---------------------------------------------------------

def main():
    print("\nLLM EVALUATION PRACTICE")
    print("Model:", MODEL)

    single_answer_accuracy = run_single_answer_evaluation()
    rubric_result = run_rubric_evaluation()
    expert_result = run_expert_evaluation()

    print("\n" + "=" * 60)
    print("FINAL EVALUATION SUMMARY")
    print("=" * 60)

    print(
        f"Single-answer accuracy: "
        f"{single_answer_accuracy:.2%}"
    )

    print(
        "Rubric evaluation completed: "
        f"{'Yes' if rubric_result else 'No'}"
    )

    print(
        "Expert-answer comparison: "
        f"{expert_result}"
    )

    print("\nEvaluation practice completed successfully.")


if __name__ == "__main__":
    main()