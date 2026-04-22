# Exam Answer Template Generator

Generate a reusable answer scaffold from an exam question.

## Included interfaces

- **Web app (Flask):** paste a question and generate a template in the browser.
- **CLI tool:** generate the same template from the terminal.

## Quick start

### Install dependencies

```bash
python3 -m pip install flask pytest
```

### Run the web app

```bash
python3 app.py
```

Open `http://127.0.0.1:5000`.

### Run the CLI

```bash
python3 exam_template.py "Explain the causes of the French Revolution."
```

## CLI usage details

Tiny CLI that takes an exam question and outputs a structured answer template.

```bash
python3 exam_template.py "Discuss photosynthesis in plants."
```

### Run tests

```bash
python3 -m pytest -q
```

## Generated template sections

- Restate the task
- Key concepts and definitions
- Step-by-step response plan
- Full answer draft scaffold
- Evidence and examples
- Final submission checklist
