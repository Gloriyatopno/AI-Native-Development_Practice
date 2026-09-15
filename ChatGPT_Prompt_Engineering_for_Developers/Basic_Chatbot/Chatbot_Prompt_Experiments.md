# Basic Conversational AI Chatbot

## Topic

Conversational AI

## Project

StudyBuddy Chatbot using Groq API

---

## Objective

The objective of this project is to build a simple conversational AI chatbot using the Groq API.

The chatbot demonstrates:

- System instructions
- User instructions
- Conversation history
- Conversational responses
- Friendly and clear communication
- API-based chatbot interaction

---

## API Used

- API: Groq API
- Programming Language: Python
- Python Library: groq
- Environment Variable Library: python-dotenv
- Model: openai/gpt-oss-20b

The Groq API is used instead of the OpenAI API.

---

## System Instruction

The chatbot uses the following system instruction:

> You are StudyBuddy, a friendly and helpful AI assistant for a college student.
>
> Your responsibilities:
> 1. Explain technical topics in simple words.
> 2. Give practical examples when useful.
> 3. Keep answers clear and not unnecessarily long.
> 4. Ask a helpful follow-up question when the user's request is unclear.
> 5. Maintain a friendly and encouraging tone.

The system instruction defines the chatbot's behavior and personality.

---

## User Instructions

The user can enter messages such as:

- Hello
- Explain Python in simple words.
- What is a variable?
- Give me an example of a for loop.
- Explain APIs.
- What is GitHub?

The chatbot sends these user messages to the Groq API and displays the generated responses.

---

## Conversation History

The chatbot stores messages in a list called `messages`.

The list contains:

1. System message
2. User messages
3. Assistant responses

Example:

```python
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot."
    },
    {
        "role": "user",
        "content": "Hello"
    },
    {
        "role": "assistant",
        "content": "Hi! How can I help you?"
    }
]