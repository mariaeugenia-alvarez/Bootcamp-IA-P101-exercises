from src.sentences.vowel_or_consonant.solution import solution


def test_solution():
    # Test case
    assert solution("x") == "consonant"
    assert solution("e") == "vowel"
    assert solution("z") == "consonant"
    assert solution("y") == "ambiguous"
    assert solution("a") == "vowel"
