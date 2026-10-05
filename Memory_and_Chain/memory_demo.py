import os
import warnings

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import (
    ConversationBufferMemory,
    ConversationBufferWindowMemory,
)

warnings.filterwarnings("ignore")
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

MODEL_NAME = "openai/gpt-oss-20b"


llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.0,
)


print("\n" + "=" * 60)
print("1. CONVERSATION BUFFER MEMORY")
print("=" * 60)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False,
)

response1 = conversation.predict(
    input="Hi, my name is Gloriya."
)

response2 = conversation.predict(
    input="What is 1 + 1?"
)

response3 = conversation.predict(
    input="What is my name?"
)

print("User: Hi, my name is Gloriya.")
print("AI:", response1)

print("\nUser: What is 1 + 1?")
print("AI:", response2)

print("\nUser: What is my name?")
print("AI:", response3)

print("\nStored conversation memory:")
print(memory.buffer)


print("\n" + "=" * 60)
print("2. MANUALLY SAVING CONTEXT")
print("=" * 60)

manual_memory = ConversationBufferMemory()

manual_memory.save_context(
    {"input": "Hi"},
    {"output": "What's up?"}
)

manual_memory.save_context(
    {"input": "Not much, just learning LangChain."},
    {"output": "That's great!"}
)

print(manual_memory.load_memory_variables({}))


print("\n" + "=" * 60)
print("3. CONVERSATION BUFFER WINDOW MEMORY")
print("=" * 60)

window_memory = ConversationBufferWindowMemory(k=1)

window_memory.save_context(
    {"input": "Hi"},
    {"output": "What's up?"}
)

window_memory.save_context(
    {"input": "Not much, just hanging."},
    {"output": "Cool!"}
)

print("Window memory with k=1:")
print(window_memory.load_memory_variables({}))

print("\nThe window memory keeps only the most recent conversation exchange.")