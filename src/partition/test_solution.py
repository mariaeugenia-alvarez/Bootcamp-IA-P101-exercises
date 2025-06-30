from partition.solution import partition_list, es_par


def test_solution():
    # Test validation
    assert es_par(2) is True
    assert es_par(1) is False
    assert partition_list([1, 2, 3, 4], es_par) == {"pasan": [2, 4], "no pasan": [1, 3]}
    assert partition_list([], es_par) == {"pasan": [], "no pasan": []}
