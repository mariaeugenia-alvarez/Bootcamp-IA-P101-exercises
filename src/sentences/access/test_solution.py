from sentences.access.solution import solution


def test_solution():
    # Test case
    assert solution("admin", 3) is True
    assert solution("usuario", 9) is True
    assert solution("usuario", 22) is False
    assert solution("invitado", 15) is True
    assert solution("invitado", 8) is False
