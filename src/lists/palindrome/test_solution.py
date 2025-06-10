from src.lists.palindrome.solution import solution

def test_solution():
    #Test case 
    assert solution("oso") == True
    assert solution("reconocer") == True
    assert solution("niña") == False
    assert solution("alla") == True
    assert solution("") == False
    assert solution("Alla") == True