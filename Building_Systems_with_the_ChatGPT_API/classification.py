import os
import json
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=API_KEY)

MODEL = "openai/gpt-oss-20b"


def classify_customer_query(user_query):
    delimiter = "####"

    system_message = f"""
You are a customer service query classification assistant.

The customer query will be provided between {delimiter} characters.

Classify the query into:
1. A primary category
2. A secondary category

Return only valid JSON using these keys:
"primary"
"secondary"

Primary categories:
- Billing
- Technical Support
- Account Management
- General Inquiry

Billing secondary categories:
- Unsubscribe or upgrade
- Add a payment method
- Explanation for charge
- Dispute a charge

Technical Support secondary categories:
- General troubleshooting
- Device compatibility
- Software updates

Account Management secondary categories:
- Password reset
- Update personal information
- Close account
- Account security

General Inquiry secondary categories:
- Product information
- Pricing
- Feedback
- Speak to a human

Do not add explanations outside the JSON.
"""

    user_message = f"{delimiter}{user_query}{delimiter}"

    messages = [
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0,
        max_tokens=150
    )

    result = response.choices[0].message.content.strip()

    try:
        classification = json.loads(result)
        return classification
    except json.JSONDecodeError:
        return {
            "error": "The model did not return valid JSON.",
            "raw_response": result
        }


def main():
    customer_queries = [
        "I want to delete my profile and all of my user data",
        "Tell me more about your flat screen TVs",
        "I was charged twice for the same subscription",
        "How can I reset my password?",
        "Is this software compatible with my laptop?"
    ]

    for query in customer_queries:
        print("\nCustomer Query:")
        print(query)

        result = classify_customer_query(query)

        print("Classification:")
        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()