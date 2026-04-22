from exam_template import build_template


def test_build_template_includes_question():
    out = build_template("Define osmosis.")
    assert "Define osmosis." in out
    assert "Tailored Answer Blueprint" in out


def test_build_template_extracts_task_and_keywords():
    out = build_template(
        "Explain and compare the causes of the French Revolution in 250 words and include two examples."
    )
    low = out.lower()
    assert "primary task verb(s): compare, explain" in low or "primary task verb(s): explain, compare" in low
    assert "french" in low
    assert "revolution" in low
    assert "250 words" in low
    assert "include two examples" in low
