#!/usr/bin/env python3
"""Generate a reusable answer template from an exam question."""

from __future__ import annotations

import argparse
import re
import textwrap
from collections import Counter

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "to",
    "was",
    "were",
    "what",
    "which",
    "with",
    "your",
}

TASK_VERBS = [
    "analyze",
    "argue",
    "assess",
    "compare",
    "contrast",
    "criticize",
    "define",
    "describe",
    "discuss",
    "evaluate",
    "explain",
    "identify",
    "illustrate",
    "justify",
    "outline",
    "summarize",
]


def extract_task_verbs(question: str) -> list[str]:
    lower = question.lower()
    found = [verb for verb in TASK_VERBS if re.search(rf"\b{verb}\b", lower)]
    return found or ["answer"]


def extract_constraints(question: str) -> list[str]:
    patterns = [
        r"\b\d+\s*(?:words?|pages?|minutes?|hours?)\b",
        r"\b(?:at least|no more than|minimum|maximum)\b[^,.!?;]*",
        r"\b(?:use|include|cite|reference)\b[^,.!?;]*",
    ]

    constraints: list[str] = []
    for pattern in patterns:
        for match in re.finditer(pattern, question, flags=re.IGNORECASE):
            snippet = match.group(0).strip(" .,")
            if snippet and snippet not in constraints:
                constraints.append(snippet)

    return constraints


def extract_keywords(question: str, limit: int = 6) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z\-']+", question.lower())
    filtered = [token for token in tokens if token not in STOPWORDS and len(token) > 2]
    if not filtered:
        return []

    counts = Counter(filtered)
    ranked = sorted(counts.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))
    return [word for word, _ in ranked[:limit]]


def build_template(question: str) -> str:
    """Return a structured answer template tailored to the given exam question."""
    cleaned_question = question.strip()
    task_verbs = extract_task_verbs(cleaned_question)
    keywords = extract_keywords(cleaned_question)
    constraints = extract_constraints(cleaned_question)

    task_text = ", ".join(task_verbs)
    keyword_lines = "\n".join(f"- {keyword}" for keyword in keywords) or "- (add key topics from the prompt)"
    constraint_lines = "\n".join(f"- {constraint}" for constraint in constraints) or "- (no explicit constraints detected)"
    keyword_block = textwrap.indent(keyword_lines, " " * 11)
    constraint_block = textwrap.indent(constraint_lines, " " * 11)

    return textwrap.dedent(
        f"""
        Exam Question
        =============
        {cleaned_question}

        Tailored Answer Blueprint
        =========================

        1) What this question is asking you to do
           - Primary task verb(s): {task_text}
           - Rewrite the prompt in your own words:
           - Core claim/position you will defend:

        2) Key topics extracted from your question
{keyword_block}

        3) Constraints and instructions detected
{constraint_block}

        4) Answer structure (customize with your extracted topics)
           Introduction:
           - Define scope and thesis in 1-2 lines.

           Body paragraph A (topic: {keywords[0] if keywords else 'Topic 1'}):
           - Main point:
           - Supporting evidence/example:
           - Why it matters:

           Body paragraph B (topic: {keywords[1] if len(keywords) > 1 else 'Topic 2'}):
           - Main point:
           - Supporting evidence/example:
           - Why it matters:

           Body paragraph C (topic: {keywords[2] if len(keywords) > 2 else 'Topic 3'}):
           - Main point:
           - Supporting evidence/example:
           - Why it matters:

           Conclusion:
           - Synthesize the argument and directly answer the prompt.

        5) Final quality check
           - [ ] Every paragraph ties back to: {task_text}
           - [ ] Key topics from prompt are explicitly addressed
           - [ ] Detected constraints/instructions are satisfied
           - [ ] Evidence is specific and relevant
        """
    ).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a tailored answer template from an exam question."
    )
    parser.add_argument("question", help="The exam question text")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(build_template(args.question))


if __name__ == "__main__":
    main()
