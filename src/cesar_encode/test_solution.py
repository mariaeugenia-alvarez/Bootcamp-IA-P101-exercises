from src.cesar_encode.solution import transpose, to_numbers, global_dictionary

def test_solution():
    #Test case
    assert transpose("zig zag",2) == "bki bci"
    assert to_numbers ("zig", global_dictionary)==[26,8,6]

    