#!/usr/bin/env python3
"""Generate a reusable answer template from an exam question."""

from __future__ import annotations

import argparse
import textwrap


def build_template(question: str) -> str:
    """Return a structured answer template for the given exam question."""
    cleaned_question = question.strip()

    return textwrap.dedent(
        f"""
        Exam Question
        =============
        {cleaned_question}

        Answer Template
        ===============

        1) Restate the task (1-2 lines)
           - What the question is asking:
           - Scope/constraints mentioned in the prompt:

        2) Key concepts / definitions
           - Concept 1:
           - Concept 2:
           - Any formulas, rules, or frameworks needed:

        3) Step-by-step response plan
           - Step 1:
           - Step 2:
           - Step 3:

        4) Full answer draft
           Introduction:
           Body point A:
           Body point B:
           Body point C:
           Conclusion:

        5) Evidence / examples to include
           - Example or case study:
           - Data / fact / reference:

        6) Final check before submission
           - [ ] Answer directly addresses the question
           - [ ] Required terminology is used accurately
           - [ ] Logical structure is clear
           - [ ] Spelling and grammar reviewed
        """
    ).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an answer template from an exam question."
    )
    parser.add_argument("question", help="The exam question text")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print(build_template(args.question))


if __name__ == "__main__":
    main()
