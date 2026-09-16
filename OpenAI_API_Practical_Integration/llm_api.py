import os

from dotenv import load_dotenv
from groq import Groq


# Load environment variables from .env
load_dotenv()


def get_client():
    """
    Create and return the Groq API client.
    """

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Check your .env file."
        )

    return Groq(api_key=api_key)


def get_model_response(user_prompt):
    """
    Send a prompt to the Groq language model
    and return the generated response.
    """

    if not user_prompt.strip():
        raise ValueError("Prompt cannot be empty.")

    client = get_client()

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant. "
                    "Give clear and simple answers."
                )
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