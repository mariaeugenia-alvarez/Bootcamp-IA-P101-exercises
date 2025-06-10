from src.lists.sum_all_char.solution import solution

def test_solution():
    #Test case 
    assert solution(["triángulo", "cuadrado", "pentágono", "hexágono", "heptágono", "octógono", "nonágono", "decágono"]) == 67
    assert solution([]) == 0
    assert solution(["triángulo"]) == 9
   
