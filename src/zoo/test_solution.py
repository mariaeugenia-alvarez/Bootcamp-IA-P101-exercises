from zoo.solution import is_not_valid_input, get_invoice


def test_solution():
    # Test validation
    assert is_not_valid_input("-3") is True
    # Test case
    assert (
        get_invoice([2])
        == "El precio total es: 0. Baby: 1 = 0. Children: 0 = 0. Adult: 0 = 0. "
    )
    assert (
        get_invoice([2, 1])
        == "El precio total es: 0. Baby: 2 = 0. Children: 0 = 0. Adult: 0 = 0. "
    )
    assert (
        get_invoice([7, 1])
        == "El precio total es: 14. Baby: 1 = 0. Children: 1 = 14. Adult: 0 = 0. "
    )
    assert (
        get_invoice([7, 1, 40])
        == "El precio total es: 37. Baby: 1 = 0. Children: 1 = 14. Adult: 1 = 23. "
    )
