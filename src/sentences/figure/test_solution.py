from src.sentences.figure.solution import solution


def test_solution():
    # Test case
    assert solution(3) == "triangulo"
    assert solution(8) == "octagono"
    assert solution(12) == "error: número fuera de rango"
