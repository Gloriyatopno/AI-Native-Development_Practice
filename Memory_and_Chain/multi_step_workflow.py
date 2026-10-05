import os
import warnings

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import LLMChain, SequentialChain
from langchain_core.prompts import ChatPromptTemplate

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


# ============================================================
# MULTI-STEP WORKFLOW
# ============================================================

print("\n" + "=" * 60)
print("MULTI-STEP LLM WORKFLOW")
print("=" * 60)


review = """
This product is excellent and arrived in two days.
The quality is very good for the price, although the
packaging was slightly damaged. I would recommend it
to other customers.
"""


# ------------------------------------------------------------
# Chain 1: Summarize the review
# ------------------------------------------------------------

summary_prompt = ChatPromptTemplate.from_template(
    "Summarize the following customer review in one sentence:\n\n"
    "{review}"
)

chain_one = LLMChain(
    llm=llm,
    prompt=summary_prompt,
    output_key="summary"
)


# ------------------------------------------------------------
# Chain 2: Analyze sentiment
# ------------------------------------------------------------

sentiment_prompt = ChatPromptTemplate.from_template(
    "Identify the sentiment of the following review.\n"
    "Return only one word: Positive, Negative, or Neutral.\n\n"
    "{review}"
)

chain_two = LLMChain(
    llm=llm,
    prompt=sentiment_prompt,
    output_key="sentiment"
)


# ------------------------------------------------------------
# Chain 3: Generate response using previous outputs
# ------------------------------------------------------------

response_prompt = ChatPromptTemplate.from_template(
    "Write a short and polite customer-service response.\n\n"
    "Review summary: {summary}\n"
    "Sentiment: {sentiment}"
)

chain_three = LLMChain(
    llm=llm,
    prompt=response_prompt,
    output_key="customer_response"
)


# ------------------------------------------------------------
# Overall Sequential Chain
# ------------------------------------------------------------

overall_chain = SequentialChain(
    chains=[
        chain_one,
        chain_two,
        chain_three
    ],
    input_variables=["review"],
    output_variables=[
        "summary",
        "sentiment",
        "customer_response"
    ],
    verbose=False
)


result = overall_chain.invoke({
    "review": review
})


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\nOriginal review:")
print(review)

print("\nStep 1 — Summary:")
print(result["summary"])

print("\nStep 2 — Sentiment:")
print(result["sentiment"])

print("\nStep 3 — Customer Response:")
print(result["customer_response"])

print("\nWorkflow:")
print(
    "Review -> Summary + Sentiment -> "
    "Customer Response"
)