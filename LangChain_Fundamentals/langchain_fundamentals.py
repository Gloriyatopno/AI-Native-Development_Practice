import os
import json

from dotenv import load_dotenv
from groq import Groq

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.output_parsers.structured import (
    ResponseSchema,
    StructuredOutputParser,
)


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")


MODEL_NAME = "openai/gpt-oss-20b"


# ============================================================
# 1. DIRECT API CALL
# ============================================================

print("\n" + "=" * 60)
print("1. DIRECT GROQ API CALL")
print("=" * 60)

direct_client = Groq(api_key=api_key)

direct_prompt = "What is an API? Explain it in one simple sentence."

direct_response = direct_client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": direct_prompt
        }
    ],
    temperature=0.0,
)

direct_answer = direct_response.choices[0].message.content

print("Prompt:", direct_prompt)
print("Response:", direct_answer)


# ============================================================
# 2. LANGCHAIN MODEL + PROMPT TEMPLATE
# ============================================================

print("\n" + "=" * 60)
print("2. LANGCHAIN MODEL + PROMPT TEMPLATE")
print("=" * 60)

chat = ChatGroq(
    model=MODEL_NAME,
    temperature=0.0,
)


template_string = """
Translate the text delimited by triple backticks
into a style that is {style}.

text: ```{text}```
"""

prompt_template = ChatPromptTemplate.from_template(template_string)


customer_style = """
American English in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid flew off and
splattered me kitchen walls with smoothie!
And to make matters worse, the warranty don't cover
the cost of cleaning up me kitchen.
I need yer help right now, matey!
"""

customer_messages = prompt_template.format_messages(
    style=customer_style,
    text=customer_email,
)

print("Prompt variables:", prompt_template.input_variables)

customer_response = chat.invoke(customer_messages)

print("\nLangChain response:")
print(customer_response.content)


# ============================================================
# 3. REUSING THE SAME PROMPT TEMPLATE
# ============================================================

print("\n" + "=" * 60)
print("3. REUSING THE PROMPT TEMPLATE")
print("=" * 60)

service_reply = """
Hey there customer, the warranty does not cover cleaning
expenses for your kitchen because it's your fault that
you misused your blender by forgetting to put the lid on
before starting the blender. Tough luck! See ya!
"""

service_style_pirate = """
a polite tone that speaks in English Pirate
"""

service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply,
)

service_response = chat.invoke(service_messages)

print("Reused template response:")

if service_response.content:
    print(service_response.content)
else:
    print("No response returned. Trying the reusable prompt again...")

    service_response = chat.invoke(
        prompt_template.format_messages(
            style="polite English Pirate",
            text=service_reply
        )
    )

    print(service_response.content)


# ============================================================
# 4. OUTPUT PARSER
# ============================================================

print("\n" + "=" * 60)
print("4. STRUCTURED OUTPUT PARSER")
print("=" * 60)

customer_review = """
This leaf blower is pretty amazing. It has four settings:
candle blower, gentle breeze, windy city, and tornado.

It arrived in two days, just in time for my wife's
anniversary present.

I think my wife liked it so much she was speechless.

So far I've been the only one using it, and I've been
using it every other morning to clear the leaves on our lawn.

It's slightly more expensive than the other leaf blowers
out there, but I think it's worth it for the extra features.
"""


gift_schema = ResponseSchema(
    name="gift",
    description=(
        "Was the item purchased as a gift for someone else? "
        "Answer True if yes, False if not or unknown."
    ),
)

delivery_days_schema = ResponseSchema(
    name="delivery_days",
    description=(
        "How many days did it take for the product to arrive? "
        "If this information is not found, output -1."
    ),
)

price_value_schema = ResponseSchema(
    name="price_value",
    description=(
        "Extract any sentences about the value or price, "
        "and output them as a comma separated Python list."
    ),
)

response_schemas = [
    gift_schema,
    delivery_days_schema,
    price_value_schema,
]

output_parser = StructuredOutputParser.from_response_schemas(
    response_schemas
)

format_instructions = output_parser.get_format_instructions()


# ============================================================
# 5. PROMPT + PARSER WORKFLOW
# ============================================================

print("\n" + "=" * 60)
print("5. PROMPT + PARSER WORKFLOW")
print("=" * 60)

review_template = """
For the following customer review, extract this information:

gift:
Was the item purchased as a gift for someone else?
Answer True if yes, False if not or unknown.

delivery_days:
How many days did it take for the product to arrive?
If this information is not found, output -1.

price_value:
Extract any sentences about the value or price,
and output them as a comma separated Python list.

Text:
{text}

{format_instructions}
"""

review_prompt = ChatPromptTemplate.from_template(review_template)

review_messages = review_prompt.format_messages(
    text=customer_review,
    format_instructions=format_instructions,
)

review_response = chat.invoke(review_messages)

print("Raw LLM output:")
print(review_response.content)


# Parse the LLM output into a Python dictionary
output_dict = output_parser.parse(review_response.content)

print("\nParsed Python dictionary:")
print(output_dict)

print("\nType of parsed output:")
print(type(output_dict))

print("\nExtracted values:")
print("gift =", output_dict.get("gift"))
print("delivery_days =", output_dict.get("delivery_days"))
print("price_value =", output_dict.get("price_value"))


# ============================================================
# 6. BASIC LANGCHAIN WORKFLOW SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("6. WORKFLOW SUMMARY")
print("=" * 60)

print(
    "User/Input Text -> ChatPromptTemplate -> ChatGroq "
    "-> LLM Response -> StructuredOutputParser -> Python Dictionary"
)


# Small JSON validation demonstration
print("\nDictionary can also be converted to JSON:")
print(json.dumps(output_dict, indent=2))