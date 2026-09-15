import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env
load_dotenv()

# Read the API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

# Create Groq client
client = Groq(api_key=api_key)

# System instruction
SYSTEM_INSTRUCTION = """
You are StudyBuddy, a friendly and helpful AI assistant for a college student.

Your responsibilities:
1. Explain technical topics in simple words.
2. Give practical examples when useful.
3. Keep answers clear and not unnecessarily long.
4. Ask a helpful follow-up question when the user's request is unclear.
5. Maintain a friendly and encouraging tone.
"""

# Conversation history
messages = [
    {
        "role": "system",
        "content": SYSTEM_INSTRUCTION
    }
]


def get_chatbot_response(user_message):
    """
    Add the user's message to the conversation,
    send the conversation to Groq,
    and return the assistant's response.
    """

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    assistant_message = response.choices[0].message.content

    messages.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )

    return assistant_message


def main():
    print("=" * 50)
    print("Welcome to StudyBuddy Chatbot")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("=" * 50)

    while True:
        user_message = input("\nYou: ").strip()

        if user_message.lower() in ["exit", "quit"]:
            print("\nStudyBuddy: Goodbye! Keep learning! 😊")
            break

        if not user_message:
            print("StudyBuddy: Please enter a message.")
            continue

        try:
            assistant_response = get_chatbot_response(user_message)
            print(f"\nStudyBuddy: {assistant_response}")

        except Exception as error:
            print(f"\nError: {error}")
            print("Please check your API key and internet connection.")


if __name__ == "__main__":
    main()