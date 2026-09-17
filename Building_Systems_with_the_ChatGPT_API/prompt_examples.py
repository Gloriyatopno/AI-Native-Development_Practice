import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=API_KEY)

MODEL = "openai/gpt-oss-20b"


def get_response(messages, temperature=0):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=150
    )

    content = response.choices[0].message.content

    if not content:
        return "[No response returned by the model]"

    return content.strip()


customer_query = "I want to delete my profile and all of my user data"


# Prompt 1: Basic prompt
messages_1 = [
    {
        "role": "user",
        "content": "Classify this customer query as Billing, Technical Support, "
                   "Account Management, or General Inquiry.\n\n"
                   "Customer query: " + customer_query
    }
]

print("PROMPT 1: BASIC PROMPT")
print(get_response(messages_1))


# Prompt 2: Clear categories
messages_2 = [
    {
        "role": "system",
        "content": """
Classify customer queries into one of these categories:
- Billing
- Technical Support
- Account Management
- General Inquiry

Return only the primary category.
"""
    },
    {
        "role": "user",
        "content": customer_query
    }
]

print("\nPROMPT 2: CLEAR CATEGORY PROMPT")
print(get_response(messages_2))


# Prompt 3: Structured JSON output
messages_3 = [
    {
        "role": "system",
        "content": """
Classify the customer query.

Primary categories:
- Billing
- Technical Support
- Account Management
- General Inquiry

Return only valid JSON using this format:
{
    "primary": "category",
    "secondary": "subcategory"
}
"""
    },
    {
        "role": "user",
        "content": customer_query
    }
]

print("\nPROMPT 3: STRUCTURED JSON PROMPT")
print(get_response(messages_3))