from p_language.solution import convert_char, p_sentence


def test_solution():
    # Test case
    assert convert_char("a", "p") == "apa"
    assert convert_char("i", "p") == "ipi"
    assert convert_char("B", "p") == "B"
    assert p_sentence("Basico", "z") == "Bazasizicozo"
    assert p_sentence("Raro", "t") == "Rataroto"
    assert p_sentence("Hola mundo", "p") == "Hopolapa mupundopo"
