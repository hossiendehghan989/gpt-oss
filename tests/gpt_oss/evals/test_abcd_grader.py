from gpt_oss.evals.abcd_grader import extract_abcd


def test_valid_answer_declarations_are_still_extracted():
    cases = {
        "Answer: C": "C",
        "**Answer:** B": "B",
        "The answer is (D).": "D",
        r"\boxed{A}": "A",
        "D) The fourth option.": "D",
        "**D**": "D",
    }

    for text, expected in cases.items():
        assert extract_abcd(text) == expected


def test_prose_starting_with_answer_letters_is_not_an_answer():
    cases = [
        "As an AI I cannot help with that.",
        "Because the data is insufficient, I cannot decide.",
        "Clearly the answer is B.",
        "Data not available.",
        "I cannot answer a question about this.",
        "Answer: 42",
        "Answer: Both are correct",
    ]

    for text in cases:
        assert extract_abcd(text) is None


def test_explicit_answer_later_in_prose_is_preserved():
    assert extract_abcd("Clearly, the answer is (B).") == "B"
    assert extract_abcd("The final choice is C.") is None
