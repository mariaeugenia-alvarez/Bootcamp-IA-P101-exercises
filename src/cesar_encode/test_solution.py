from src.cesar_encode.solution import transpose, to_numbers, global_dictionary, to_string

def test_solution():
    #Test case
    #assert transpose("zig zag",2) == "bki bci"
    assert to_numbers("zig", global_dictionary) == [26,8,6]
    assert to_string([26,8,6], global_dictionary) == "zig"
    assert to_string(to_numbers("zig", global_dictionary), global_dictionary) == "zig"
    assert to_numbers(to_string([26,8,6], global_dictionary), global_dictionary) == [26,8,6]