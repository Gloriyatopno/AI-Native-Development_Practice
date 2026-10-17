
import uuid

from flask import Flask, redirect, render_template_string, request, url_for
from langgraph.types import Command

from essay_workflow import open_graph

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Essay Writer Agent</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 35px auto;
            padding: 0 18px;
            line-height: 1.6;
            color: #222;
        }
        textarea, input {
            width: 100%;
            box-sizing: border-box;
            padding: 10px;
            margin: 8px 0 16px;
        }
        button {
            padding: 10px 16px;
            margin: 4px 6px 4px 0;
            cursor: pointer;
        }
        .draft {
            background: #f6f6f6;
            padding: 18px;
            border-radius: 6px;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
        }
        .status {
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Essay Writer Agent</h1>
    <p>Research a topic, review the draft, and approve or request revisions.</p>

    {% if not thread_id %}
        <form method="post" action="{{ url_for('home') }}">
            <label for="topic"><strong>Essay topic</strong></label>
            <input
                id="topic"
                name="topic"
                required
                maxlength="300"
                placeholder="Enter your essay topic"
            >
            <button type="submit">Research and write</button>
        </form>
    {% else %}
        <p><strong>Topic:</strong> {{ topic }}</p>
        <p class="status">Status: {{ status }}</p>
        <p>Revisions completed: {{ revision_count }}</p>

        {% if draft %}
            <h2>Essay draft</h2>
            <div class="draft">{{ draft }}</div>
        {% endif %}

        {% if pending_review %}
            <h2>Human review</h2>
            <p>Read the essay and approve it or request a revision.</p>

            <form method="post"
                  action="{{ url_for('review', thread_id=thread_id) }}">
                <label for="feedback"><strong>Revision feedback</strong></label>
                <textarea
                    id="feedback"
                    name="feedback"
                    rows="4"
                    placeholder="Describe what should be improved if requesting a revision."
                ></textarea>

                <button type="submit" name="action" value="approve">
                    Approve essay
                </button>
                <button type="submit" name="action" value="revise">
                    Request revision
                </button>
            </form>
        {% elif status == "approved" %}
            <h2>Essay approved</h2>
            <p>The workflow is complete.</p>
        {% else %}
            <p>The workflow has ended. Status: {{ status }}</p>
        {% endif %}

        <p><a href="{{ url_for('home') }}">Start a new essay</a></p>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template_string(
            PAGE,
            thread_id=None,
            topic="",
            draft="",
            status="not_started",
            revision_count=0,
            pending_review=False,
        )

    topic = request.form.get("topic", "").strip()

    if not topic:
        return "Please provide an essay topic.", 400

    thread_id = f"essay-{uuid.uuid4().hex[:12]}"
    config = {"configurable": {"thread_id": thread_id}}

    initial_state = {
        "topic": topic,
        "research": "",
        "draft": "",
        "review_feedback": "",
        "revision_count": 0,
        "approved": False,
        "status": "started",
    }

    graph, connection = open_graph()
    try:
        graph.invoke(initial_state, config=config)
    finally:
        connection.close()

    return redirect(url_for("review", thread_id=thread_id))


@app.route("/review/<thread_id>", methods=["GET", "POST"])
def review(thread_id):
    config = {"configurable": {"thread_id": thread_id}}

    graph, connection = open_graph()

    try:
        if request.method == "POST":
            action = request.form.get("action", "")
            feedback = request.form.get("feedback", "").strip()

            if action not in {"approve", "revise"}:
                return "Invalid review action.", 400

            if action == "revise" and not feedback:
                return "Please enter feedback before requesting a revision.", 400

            decision = {
                "action": action,
                "feedback": feedback,
            }

            graph.invoke(Command(resume=decision), config=config)

            return redirect(url_for("review", thread_id=thread_id))

        snapshot = graph.get_state(config)
        values = snapshot.values or {}

        pending_review = bool(snapshot.next)

        return render_template_string(
            PAGE,
            thread_id=thread_id,
            topic=values.get("topic", ""),
            draft=values.get("draft", ""),
            status=values.get("status", "unknown"),
            revision_count=values.get("revision_count", 0),
            pending_review=pending_review,
        )
    finally:
        connection.close()


if __name__ == "__main__":
    app.run(debug=False)
