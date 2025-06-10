from src.sentences.access.solution import solution

def test_solution():
    #Test case 
    assert solution('admin',3) == True
    assert solution('usuario',9) == True
    assert solution('usuario',22) == False
    assert solution('invitado',15) == True
    assert solution('invitado',8) == False
