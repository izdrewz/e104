# Exam Answer Template Generator

Generate structured answer outlines from exam questions.

This repo includes two interfaces:
- **Web app (Flask):** interactive browser form for quick drafting.
- **CLI tool:** terminal command for scriptable workflows.

## Run the web app

```bash
python3 -m pip install flask
python3 app.py
```

Open: `http://127.0.0.1:5000`

## Run the CLI

```bash
python3 exam_template.py "Explain the causes of the French Revolution."
```

## Example output sections

The generated template includes:
1. Task restatement
2. Key concepts / definitions
3. Step-by-step response plan
4. Full answer draft scaffold
5. Evidence / examples
6. Final submission checklist
