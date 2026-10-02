from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os
import markdown
import bleach
import logging

load_dotenv()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024  # 16 KB request limit

logging.basicConfig(level=logging.INFO)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is not configured.")

client = Groq(api_key=api_key)

ALLOWED_TAGS = [
    "p", "br", "strong", "em", "b", "i",
    "h1", "h2", "h3", "h4",
    "ul", "ol", "li",
    "blockquote", "code", "pre",
    "table", "thead", "tbody", "tr", "th", "td",
    "a", "hr"
]

ALLOWED_ATTRIBUTES = {
    "a": ["href", "title"]
}


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    error_message = ""
    user_prompt = ""

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()

        if not user_prompt:
            error_message = "Please enter a prompt."

        elif len(user_prompt) > 2000:
            error_message = "Your prompt must be 2000 characters or fewer."

        else:
            try:
                result = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a helpful AI text assistant. "
                                "Answer clearly and concisely."
                            )
                        },
                        {
                            "role": "user",
                            "content": user_prompt
                        }
                    ],
                    temperature=0.7,
                    max_tokens=500
                )

                raw_response = result.choices[0].message.content or ""

                html_response = markdown.markdown(
                    raw_response,
                    extensions=["tables", "fenced_code"]
                )

                response = bleach.clean(
                    html_response,
                    tags=ALLOWED_TAGS,
                    attributes=ALLOWED_ATTRIBUTES,
                    protocols=["http", "https", "mailto"],
                    strip=True
                )

            except Exception as error:
                logging.error(
                    "AI request failed: %s",
                    type(error).__name__
                )
                error_message = (
                    "Sorry, something went wrong. Please try again."
                )

    return render_template(
        "index.html",
        response=response,
        error_message=error_message,
        user_prompt=user_prompt
    )


if __name__ == "__main__":
    app.run(debug=False)