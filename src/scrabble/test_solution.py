from scrabble.solution import (
    get_points,
    get_sorted_keys,
    score,
    global_scrabble_dictionary,
    remove,
    substring,
)


def test_solution():
    # Test case
    assert substring("PERRO", "RR") == 1
    assert substring("PERRO", "R") == 2
    assert substring("PERRO", "A") == 0
    assert remove("PERRO", "RR") == "PEO"
    assert remove("PERRO", "R") == "PEO"
    assert get_sorted_keys({"A": 1, "RR": 2, "B": 2}) == ["RR", "A", "B"]
    assert get_sorted_keys({"A": 1, "RR": 2, "B": 2, "CH": 1}) == ["RR", "CH", "A", "B"]
    assert get_sorted_keys({"A": 1, "RR": 2, "B": 2, "CHA": 1}) == [
        "CHA",
        "RR",
        "A",
        "B",
    ]
    assert get_points(1, "RR", global_scrabble_dictionary) == 8
    assert score("PERRO", global_scrabble_dictionary) == (
        13,
        {
            "E": 1,
            "O": 1,
            "P": 1,
            "RR": 1,
        },
    )
    assert score("CONCHA", global_scrabble_dictionary) == (
        11,
        {"A": 1, "C": 1, "CH": 1, "N": 1, "O": 1},
    )
    assert score("PORRO", global_scrabble_dictionary) == (
        13,
        {
            "P": 1,
            "O": 2,
            "RR": 1,
        },
    )
