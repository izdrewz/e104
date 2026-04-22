#!/usr/bin/env python3
"""Web app for generating exam answer templates."""

from __future__ import annotations

from flask import Flask, render_template_string, request

from exam_template import build_template

app = Flask(__name__)

PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Exam Answer Template Generator</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 2rem; max-width: 900px; }
      textarea { width: 100%; min-height: 120px; margin-bottom: 1rem; }
      button { padding: 0.6rem 1rem; }
      pre { white-space: pre-wrap; background: #f5f5f5; padding: 1rem; border-radius: 8px; }
    </style>
  </head>
  <body>
    <h1>Exam Answer Template Generator</h1>
    <form method="post">
      <label for="question"><strong>Exam question</strong></label>
      <textarea id="question" name="question" placeholder="Type your exam question here...">{{ question }}</textarea>
      <br />
      <button type="submit">Generate template</button>
    </form>

    {% if output %}
      <h2>Generated Template</h2>
      <pre>{{ output }}</pre>
    {% endif %}
  </body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    question = ""
    output = ""

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            output = build_template(question)

    return render_template_string(PAGE, question=question, output=output)


if __name__ == "__main__":
    app.run(debug=True)
