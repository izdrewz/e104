from exam_template import build_template


def test_build_template_includes_question():
    out = build_template("Define osmosis.")
    assert "Define osmosis." in out
    assert "Answer Template" in out


def test_build_template_has_expected_sections():
    out = build_template("Sample?")
    assert "1) Restate the task" in out
    assert "2) Key concepts / definitions" in out
    assert "6) Final check before submission" in out
