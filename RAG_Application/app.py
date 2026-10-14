import os

from flask import Flask, render_template_string, request
from dotenv import load_dotenv
from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

app = Flask(__name__)

client = Groq(api_key=api_key)

MODEL_NAME = "openai/gpt-oss-20b"


# ============================================================
# LOAD DOCUMENT
# ============================================================

with open("documents.txt", "r", encoding="utf-8") as file:
    document_text = file.read()


# Split the document into smaller sections
documents = [
    section.strip()
    for section in document_text.split("\n\n")
    if section.strip()
]


# ============================================================
# CREATE VECTOR REPRESENTATIONS
# ============================================================

vectorizer = TfidfVectorizer()

document_vectors = vectorizer.fit_transform(documents)


# ============================================================
# RETRIEVE RELEVANT DOCUMENTS
# ============================================================

def retrieve_context(question, top_k=5):
    question_vector = vectorizer.transform([question])

    scores = cosine_similarity(
        question_vector,
        document_vectors
    )[0]

    top_indices = scores.argsort()[::-1][:top_k]

    results = []

    for index in top_indices:
        results.append(
            {
                "text": documents[index],
                "score": scores[index]
            }
        )

    return results


# ============================================================
# GENERATE ANSWER USING RETRIEVED CONTEXT
# ============================================================

def generate_answer(question, retrieved_documents):

    context = "\n\n".join(
        item["text"]
        for item in retrieved_documents
        if item["score"] > 0
    )

    if not context:
        return "I could not find relevant information in the supplied document."

    prompt = f"""
You are an assistant answering questions about the AI Text Assistant application.

Use only the supplied context to answer the question.

Context:
{context}

Question:
{question}

Give a clear and concise answer.

If the answer is not available in the context, say:
"I could not find that information in the supplied document."
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.0,
        max_tokens=300
    )

    return response.choices[0].message.content


# ============================================================
# FLASK APPLICATION
# ============================================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAG Application</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f6f8;
            margin: 0;
            padding: 40px 20px;
        }

        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        }

        textarea {
            width: 100%;
            box-sizing: border-box;
            padding: 12px;
            margin-top: 15px;
            border: 1px solid #ccc;
            border-radius: 8px;
            resize: vertical;
            font-size: 16px;
        }

        button {
            margin-top: 15px;
            padding: 11px 20px;
            border: none;
            border-radius: 8px;
            background: #222;
            color: white;
            font-size: 15px;
            cursor: pointer;
        }

        .response,
        .context {
            margin-top: 25px;
            padding: 20px;
            background: #f8f9fa;
            border-left: 4px solid #222;
            border-radius: 6px;
            line-height: 1.6;
        }

        .context-item {
            margin-bottom: 12px;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>RAG Application</h1>

    <p>
        Ask a question about the supplied application information.
    </p>

    <form method="POST">

        <textarea
            name="question"
            rows="5"
            placeholder="Ask a question..."
            required
        >{{ question }}</textarea>

        <button type="submit">Ask Question</button>

    </form>

    {% if answer %}
        <h2>Answer</h2>

        <div class="response">
            {{ answer }}
        </div>
    {% endif %}

    {% if retrieved %}
        <h2>Retrieved Context</h2>

        <div class="context">

            {% for item in retrieved %}

                <div class="context-item">
                    <strong>Similarity: {{ "%.3f"|format(item.score) }}</strong>
                    <br>
                    {{ item.text }}
                </div>

            {% endfor %}

        </div>
    {% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    question = ""
    answer = ""
    retrieved = []

    if request.method == "POST":

        question = request.form.get(
            "question",
            ""
        ).strip()

        if question:

            retrieved = retrieve_context(question)

            answer = generate_answer(
                question,
                retrieved
            )

    return render_template_string(
        HTML_TEMPLATE,
        question=question,
        answer=answer,
        retrieved=retrieved
    )


if __name__ == "__main__":
    app.run(debug=False)