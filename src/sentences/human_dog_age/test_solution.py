from src.sentences.human_dog_age.solution import solution

def test_solution():
    #Test case 1
    assert solution(1.5) == 15.75
    #Test case 1
    assert solution(4) == 29.0 
    #Test case 1
    assert solution(-2) == "Error: edad negativa"
   