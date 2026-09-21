import os
import json
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)

MODEL = "openai/gpt-oss-20b"


# Sample product information
products = {
    "SmartX ProPhone": {
        "name": "SmartX ProPhone",
        "category": "Smartphone",
        "brand": "SmartX",
        "model": "ProPhone",
        "warranty": "1 year",
        "rating": 4.5,
        "features": [
            "6.5-inch OLED display",
            "128GB storage",
            "48MP camera",
            "5G support"
        ],
        "description": "A premium smartphone designed for everyday and professional use.",
        "price": 799
    },

    "FotoSnap DSLR Camera": {
        "name": "FotoSnap DSLR Camera",
        "category": "Camera",
        "brand": "FotoSnap",
        "model": "DSLR Camera",
        "warranty": "2 years",
        "rating": 4.7,
        "features": [
            "24MP sensor",
            "4K video recording",
            "Interchangeable lenses",
            "Wi-Fi connectivity"
        ],
        "description": "A versatile DSLR camera for photography and video recording.",
        "price": 649
    },

    "CineView 8K TV": {
        "name": "CineView 8K TV",
        "category": "TV",
        "brand": "CineView",
        "model": "8K TV",
        "warranty": "2 years",
        "rating": 4.8,
        "features": [
            "75-inch 8K display",
            "HDR support",
            "Smart TV platform",
            "Dolby Atmos"
        ],
        "description": "A premium 8K television designed for an immersive home entertainment experience.",
        "price": 2499
    },

    "SoundMax Wireless Headphones": {
        "name": "SoundMax Wireless Headphones",
        "category": "Headphones",
        "brand": "SoundMax",
        "model": "Wireless Headphones",
        "warranty": "1 year",
        "rating": 4.4,
        "features": [
            "Active noise cancellation",
            "Bluetooth 5.3",
            "30-hour battery life",
            "Wireless charging"
        ],
        "description": "Wireless headphones with active noise cancellation and long battery life.",
        "price": 199
    }
}


def extract_products(user_question):
    """
    First step of the prompt chain.

    Extract product names or product categories mentioned
    in the user's question.
    """

    product_names = list(products.keys())

    categories = list(
        set(product["category"] for product in products.values())
    )

    extraction_prompt = f"""
You are a product reference extractor.

Identify the products or product categories relevant to the
customer's question.

Only use product names and categories from the lists below.

Available products:
{product_names}

Available categories:
{categories}

Return JSON only using this format:

{{
    "products": [],
    "categories": []
}}

Customer question:
####
{user_question}
####
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Extract relevant products and categories from customer questions."
                },
                {
                    "role": "user",
                    "content": extraction_prompt
                }
            ],
            temperature=0,
            max_completion_tokens=300,
            include_reasoning=False
        )

        result = response.choices[0].message.content.strip()

        if not result:
            return {"products": [], "categories": []}

        extracted = json.loads(result)

        return extracted

    except (json.JSONDecodeError, Exception) as e:
        print("Product extraction error:", e)
        return {"products": [], "categories": []}


def get_product_by_name(name):
    """Return product information using an exact product name."""

    return products.get(name)


def get_products_by_category(category):
    """Return all products belonging to a category."""

    return [
        product
        for product in products.values()
        if product["category"].lower() == category.lower()
    ]


def get_relevant_products(extracted):
    """
    Use the output from the first prompt to retrieve
    the relevant product information.
    """

    relevant_products = []

    # Get products identified by name
    for product_name in extracted.get("products", []):
        product = get_product_by_name(product_name)

        if product and product not in relevant_products:
            relevant_products.append(product)

    # Get products identified by category
    for category in extracted.get("categories", []):
        category_products = get_products_by_category(category)

        for product in category_products:
            if product not in relevant_products:
                relevant_products.append(product)

    return relevant_products


def create_product_information(relevant_products):
    """Convert product data into readable information for the next prompt."""

    if not relevant_products:
        return "No relevant product information was found."

    product_information = ""

    for product in relevant_products:
        product_information += f"""
Product: {product["name"]}
Category: {product["category"]}
Brand: {product["brand"]}
Model: {product["model"]}
Price: ${product["price"]}
Rating: {product["rating"]}/5
Warranty: {product["warranty"]}
Features: {", ".join(product["features"])}
Description: {product["description"]}

"""

    return product_information


def generate_final_response(user_question, product_information):
    """
    Second step of the prompt chain.

    Use the customer's question and the product information
    retrieved in the first step to generate the final answer.
    """

    final_prompt = f"""
You are a friendly customer service assistant.

Answer the customer's question using ONLY the product
information provided below.

Do not invent product details or prices.

If the requested information is not available, clearly
say that it is not available.

Keep the answer concise and helpful.

Product information:
####
{product_information}
####

Customer question:
####
{user_question}
####
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "Answer customer questions using only the provided product information."
                },
                {
                    "role": "user",
                    "content": final_prompt
                }
            ],
            temperature=0,
            max_completion_tokens=400,
            include_reasoning=False
        )

        result = response.choices[0].message.content.strip()

        if not result:
            return "Unable to generate a response."

        return result

    except Exception as e:
        print("Response generation error:", e)
        return "Unable to generate a response."


def process_question(user_question):
    """
    Complete multi-step prompt chaining workflow.

    Step 1: Extract products/categories
    Step 2: Retrieve product information
    Step 3: Pass retrieved information to the final prompt
    Step 4: Generate final answer
    """

    print("\n" + "=" * 60)
    print("PROMPT CHAIN WORKFLOW")
    print("=" * 60)

    print("\nCustomer question:")
    print(user_question)

    # STEP 1
    print("\nSTEP 1 - PRODUCT EXTRACTION")

    extracted = extract_products(user_question)

    print("Extracted information:")
    print(json.dumps(extracted, indent=4))

    # STEP 2
    print("\nSTEP 2 - PRODUCT LOOKUP")

    relevant_products = get_relevant_products(extracted)

    if relevant_products:
        print("Relevant products:")
        for product in relevant_products:
            print("-", product["name"])
    else:
        print("No relevant products found.")

    # STEP 3
    print("\nSTEP 3 - PREPARE INFORMATION FOR NEXT PROMPT")

    product_information = create_product_information(relevant_products)

    print(product_information)

    # STEP 4
    print("\nSTEP 4 - FINAL RESPONSE")

    final_response = generate_final_response(
        user_question,
        product_information
    )

    print(final_response)

    return final_response


if __name__ == "__main__":

    test_questions = [
        "Which camera is cheaper and what features does it have?",
        "Tell me about your TVs.",
        "Which is more highly rated, the SmartX ProPhone or the FotoSnap DSLR Camera?",
        "My router isn't working."
    ]

    for question in test_questions:
        process_question(question)