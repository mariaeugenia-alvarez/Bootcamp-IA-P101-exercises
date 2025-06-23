from cesar_encode.solution import (
    encrypt,
    transpose,
    to_numbers,
    global_dictionary,
    to_string,
)


def test_solution():
    # Test case
    assert to_numbers("zig", global_dictionary) == [26, 8, 6]
    assert to_numbers("zig zag", global_dictionary) == [26, 8, 6, " ", 26, 0, 6]
    assert to_string([26, 8, 6], global_dictionary) == "zig"
    assert to_string([26, 8, 6, " ", 26, 0, 6], global_dictionary) == "zig zag"
    assert to_string(to_numbers("zig", global_dictionary), global_dictionary) == "zig"
    assert to_numbers(to_string([26, 8, 6], global_dictionary), global_dictionary) == [
        26,
        8,
        6,
    ]
    assert encrypt([26, 8, 6], 2, global_dictionary) == [1, 10, 8]
    assert transpose("zig zag", 2) == "bki bci"
    assert transpose("bki bci", -2) == "zig zag"
