from src.lists.sum_all_list.solution import solution

def test_solution():
    #Test case 
    assert solution([3, 17, 12, 24, 6, 1, 21, 10, 14, 7]) == 115
    assert solution([]) == 0
    assert solution([3]) == 3
    assert solution([-3, 17, -12, 24, 6, 1, 21, 10, 14, 7]) == 85
