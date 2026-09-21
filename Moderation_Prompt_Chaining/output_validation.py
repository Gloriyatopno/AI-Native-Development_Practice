import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-20b"


def validate_output(customer_question, product_information, agent_response):
    """
    Check whether the generated response:
    1. Answers the customer's question.
    2. Uses the provided product information correctly.

    Returns:
        True  -> response is valid
        False -> response is invalid
    """

    validation_prompt = f"""
You are evaluating a customer service response.

Determine whether the agent response:

1. Answers the customer's question.
2. Uses the provided product information correctly.
3. Does not invent product facts, prices, ratings, or features.

Return exactly one character:

Y = response is valid
N = response is invalid

Customer question:{customer_question}

Product information:{product_information}

Agent response:{agent_response}

Return only Y or N.
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a strict customer service response evaluator. "
                        "Check answers against the supplied product information."
                    )
                },
                {
                    "role": "user",
                    "content": validation_prompt
                }
            ],
            temperature=0,
            max_completion_tokens=300,
            include_reasoning=False
        )

        result = response.choices[0].message.content.strip().upper()

        if result.startswith("Y"):
            return True

        if result.startswith("N"):
            return False

        print("Unexpected validation output:", result)
        return False

    except Exception as e:
        print("Validation error:", e)

        # Fail safely if validation cannot be completed
        return False


if __name__ == "__main__":

    customer_question = (
        "What are the features and price of the FotoSnap DSLR Camera?"
    )

    product_information = """
Product: FotoSnap DSLR Camera
Category: Camera
Brand: FotoSnap
Model: DSLR Camera
Price: $649
Rating: 4.7/5
Warranty: 2 years
Features: 24MP sensor, 4K video recording, Interchangeable lenses, Wi-Fi connectivity
Description: A versatile DSLR camera for photography and video recording.
"""

    # Correct response
    valid_response = """
The FotoSnap DSLR Camera costs $649 and has a 24MP sensor,
4K video recording, interchangeable lenses, and Wi-Fi connectivity.
"""

    # Incorrect response containing invented information
    invalid_response = """
The FotoSnap DSLR Camera costs $499 and has a 50MP sensor,
8K video recording, and a 10-year warranty.
"""

    print("OUTPUT VALIDATION TESTS")
    print("=" * 50)

    print("\nTEST 1 - VALID RESPONSE")
    print("Agent response:")
    print(valid_response)

    valid_result = validate_output(
        customer_question,
        product_information,
        valid_response
    )

    if valid_result:
        print("Validation result: VALID")
    else:
        print("Validation result: INVALID")

    print("\nTEST 2 - INVALID RESPONSE")
    print("Agent response:")
    print(invalid_response)

    invalid_result = validate_output(
        customer_question,
        product_information,
        invalid_response
    )

    if invalid_result:
        print("Validation result: VALID")
    else:
        print("Validation result: INVALID")