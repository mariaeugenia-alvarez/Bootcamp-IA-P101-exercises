from src.cesar_encode.solution import transpose

def test_solution():
    #Test case
    assert transpose("zig zag",2) == "bki bci"
    