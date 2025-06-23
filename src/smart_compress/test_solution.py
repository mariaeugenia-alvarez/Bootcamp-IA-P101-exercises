from smart_compress.solution import accumulate, chain_compress


def test_solution():
    # Test case
    assert accumulate("h", 3) == "h3"
    assert accumulate("o", 2) == "oo"
    assert chain_compress("hhhoollllla") == "h3ool5a"
    assert chain_compress("hhhoollllaa") == "h3ool4aa"
    assert chain_compress("hhhoolllaaa") == "h3ool3a3"
    assert chain_compress("hellooo") == "hello3"
    assert chain_compress("aabbcc") == "aabbcc"
    assert chain_compress("baaaad") == "ba4d"
    assert chain_compress("") == ""
    assert chain_compress(" ") == " "
    assert chain_compress("e") == "e"
    assert chain_compress("eee") == "e3"
