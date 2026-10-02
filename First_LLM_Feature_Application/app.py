from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os
import markdown

load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    user_prompt = ""

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()

        if user_prompt:
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

                response = markdown.markdown(
                    result.choices[0].message.content,
                    extensions=["tables", "fenced_code"]
                )

            except Exception as error:
                response = f"<p>Error: {error}</p>"

        else:
            response = "<p>Please enter a prompt.</p>"

    return render_template(
        "index.html",
        response=response,
        user_prompt=user_prompt
    )


if __name__ == "__main__":
    app.run(debug=True)