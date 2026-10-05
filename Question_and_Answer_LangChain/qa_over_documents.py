import os
import warnings

import numpy as np
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from langchain_community.document_loaders import CSVLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


warnings.filterwarnings("ignore")
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

MODEL_NAME = "openai/gpt-oss-20b"
FILE_NAME = "OutdoorClothingCatalog.csv"


# ============================================================
# 1. LOAD DOCUMENTS
# ============================================================

print("\n" + "=" * 60)
print("1. LOADING SAMPLE DOCUMENTS")
print("=" * 60)

loader = CSVLoader(file_path=FILE_NAME)
documents = loader.load()

print(f"Documents loaded: {len(documents)}")
print("\nFirst document:")
print(documents[0].page_content)


# ============================================================
# 2. CREATE LOCAL VECTOR REPRESENTATIONS
# ============================================================

print("\n" + "=" * 60)
print("2. CREATING DOCUMENT VECTORS")
print("=" * 60)

document_texts = [
    document.page_content
    for document in documents
]

vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(document_texts)

print("Vector representation created successfully.")
print(f"Vector matrix shape: {document_vectors.shape}")


# ============================================================
# 3. RETRIEVAL FUNCTION
# ============================================================

def retrieve_documents(query, top_k=3):
    query_vector = vectorizer.transform([query])

    similarity_scores = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    top_indices = np.argsort(similarity_scores)[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append(
            {
                "document": documents[index],
                "score": similarity_scores[index]
            }
        )

    return results


# ============================================================
# 4. LANGCHAIN LLM
# ============================================================

print("\n" + "=" * 60)
print("3. INITIALIZING LANGCHAIN LLM")
print("=" * 60)

llm = ChatGroq(
    model=MODEL_NAME,
    temperature=0.0,
)


# ============================================================
# 5. QUESTION ANSWERING
# ============================================================

qa_prompt = ChatPromptTemplate.from_template(
    """
You are answering questions about an outdoor clothing catalog.

Use only the information provided in the context below.

If the answer is not available in the context, say:
"That information is not available in the supplied catalog."

Context:
{context}

Question:
{question}

Answer clearly and concisely.
"""
)


def answer_question(question):
    retrieved = retrieve_documents(question, top_k=3)

    context_parts = []

    for item in retrieved:
        context_parts.append(item["document"].page_content)

    context = "\n\n".join(context_parts)

    messages = qa_prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    return response.content, retrieved


# ============================================================
# 6. TEST QUESTIONS
# ============================================================

test_questions = [
    "Which product provides UPF 50+ sun protection?",
    "Which clothing item is designed for heavy rain and windy mountain conditions?",
    "Which product is suitable for cold-weather hiking and provides insulation?"
]


print("\n" + "=" * 60)
print("4. Q&A TESTS")
print("=" * 60)

for number, question in enumerate(test_questions, start=1):

    answer, retrieved_documents = answer_question(question)

    print(f"\nTest {number}")
    print("-" * 40)

    print("Question:")
    print(question)

    print("\nRetrieved documents:")

    for item in retrieved_documents:
        print(
            f"- similarity={item['score']:.3f} | "
            f"{item['document'].page_content}"
        )

    print("\nAnswer:")
    print(answer)


# ============================================================
# 7. Q&A WORKFLOW
# ============================================================

print("\n" + "=" * 60)
print("5. Q&A WORKFLOW")
print("=" * 60)

print(
    "CSV Documents -> Vector Representation -> "
    "Similarity Search -> Relevant Context -> "
    "ChatGroq -> Answer"
)