import os
import warnings

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_classic.chains import LLMChain, SimpleSequentialChain
from langchain_core.prompts import ChatPromptTemplate

warnings.filterwarnings("ignore")
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

MODEL_NAME = "openai/gpt-oss-20b"

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.7,
)


# ============================================================
# 1. LLM CHAIN
# ============================================================

print("\n" + "=" * 60)
print("1. LLM CHAIN")
print("=" * 60)

prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe a company that makes {product}?"
)

chain = LLMChain(
    llm=llm,
    prompt=prompt
)

product = "Queen Size Sheet Set"

company_name = chain.run(product)

print("Product:", product)
print("Generated company name:", company_name)


# ============================================================
# 2. SIMPLE SEQUENTIAL CHAIN
# ============================================================

print("\n" + "=" * 60)
print("2. SIMPLE SEQUENTIAL CHAIN")
print("=" * 60)

first_prompt = ChatPromptTemplate.from_template(
    "What is the best name to describe a company that makes {product}?"
)

chain_one = LLMChain(
    llm=llm,
    prompt=first_prompt
)

second_prompt = ChatPromptTemplate.from_template(
    "Write a short description for the following company: {company_name}"
)

chain_two = LLMChain(
    llm=llm,
    prompt=second_prompt
)

overall_simple_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose=False
)

result = overall_simple_chain.run(product)

print("Product:", product)
print("Final result:")
print(result)


# ============================================================
# 3. WORKFLOW SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("3. CHAIN WORKFLOW")
print("=" * 60)

print(
    "Product Input -> Chain 1 -> Company Name -> "
    "Chain 2 -> Company Description"
)