from cesar_encode_generator.solution import (
    to_cesar,
    abecedario,
    cesar,
)


def test_solution():
    # Test case
    assert to_cesar("z", 2, abecedario) == "b"
    assert cesar("zig zag", 2, abecedario) == "bki bci"
