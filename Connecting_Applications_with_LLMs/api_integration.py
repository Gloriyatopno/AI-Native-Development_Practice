import os
from dotenv import load_dotenv
from groq import Groq


# Load environment variables from .env
load_dotenv()

# Read the API key securely
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

# Create the Groq client
client = Groq(api_key=api_key)


def get_model_response(user_prompt):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Give clear and simple answers."
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].message.content


print("Connecting Applications with LLMs")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        answer = get_model_response(user_input)
        print("\nAI:", answer)
        print()

    except Exception as error:
        print("\nError:", error)
        print()