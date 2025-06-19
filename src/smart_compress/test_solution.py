from src.smart_compress.solution import accumulate, chain_compress
def test_solution():
    #Test case
    assert accumulate("h",3) == "h3"
    assert accumulate("o",2) == "oo"
    assert chain_compress("hhhoollllla") == "h3ool5a"
    assert chain_compress("hhhoollllaa") == "h3ool4aa"