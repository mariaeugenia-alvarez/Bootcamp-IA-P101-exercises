from src.temporal_data.solution import numbers_incremental_series,  index_difference
def test_solution():
    #Test case
    assert index_difference(1,72,75) == {1:3}
    assert numbers_incremental_series([72,72,75,75,70,74,74,76]) == [75,74,76]


   