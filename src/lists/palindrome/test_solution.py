from src.lists.palindrome.solution import solution


def test_solution():
    # Test case
    assert solution("oso") is True
    assert solution("reconocer") is True
    assert solution("niña") is False
    assert solution("alla") is True
    assert solution("") is False
    assert solution("Alla") is True
