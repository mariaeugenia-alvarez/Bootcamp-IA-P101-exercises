from src.zoo.solution import is_not_valid_input, get_invoice

def test_solution():
    #Test validation
    assert is_not_valid_input("-3") == True
    #Test case
    assert get_invoice([]) == "El precio total es: 0. Niños de 2 años o menos: 0 = 0. Niños de 3 a 12 años: 0 = 0. Niños de 13 a 65 años: 0 = 0. "
    #asert get_invoice([" "]) == "El precio total es: 0. Niños de 2 años o menos: 0 = 0. Niños de 3 a 12 años: 0 = 0. Niños de 13 a 65 años: 0 = 0. "
    assert get_invoice([2]) == "El precio total es: 0. Niños de 2 años o menos: 1 = 0. Niños de 3 a 12 años: 0 = 0. Niños de 13 a 65 años: 0 = 0. "
    assert get_invoice([2,1]) == "El precio total es: 0. Niños de 2 años o menos: 2 = 0. Niños de 3 a 12 años: 0 = 0. Niños de 13 a 65 años: 0 = 0. "
    assert get_invoice([7,1]) == "El precio total es: 14. Niños de 2 años o menos: 1 = 0. Niños de 3 a 12 años: 1 = 14. Niños de 13 a 65 años: 0 = 0. "
    assert get_invoice([7,1,40]) == "El precio total es: 37. Niños de 2 años o menos: 1 = 0. Niños de 3 a 12 años: 1 = 14. Niños de 13 a 65 años: 1 = 23. "