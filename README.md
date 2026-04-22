# Exam Answer Template Generator

Generate a reusable answer scaffold from an exam question.

## What this project includes

- **Web app (Flask):** paste a question and generate a template in the browser.
- **CLI tool:** generate the same template from the terminal.

## Quick start

### 1) Install dependencies

```bash
python3 -m pip install flask pytest
```

### 2) Run the web app

```bash
python3 app.py
```

Open `http://127.0.0.1:5000`.

### 3) Run the CLI

```bash
python3 exam_template.py "Explain the causes of the French Revolution."
```

### 4) Run tests

```bash
python3 -m pytest -q
```

## Generated template structure

1. Restate the task
2. Key concepts / definitions
3. Step-by-step response plan
4. Full answer draft scaffold
5. Evidence / examples
6. Final submission checklist
