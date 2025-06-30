from cesar_encode_generator.solution import (
    cifrar,
    to_cesar,
    abecedario,
)


def test_solution():
    # Test case
    assert to_cesar("z", 2, abecedario) == "b"
    assert cifrar("zig zag") == "bki bci"
