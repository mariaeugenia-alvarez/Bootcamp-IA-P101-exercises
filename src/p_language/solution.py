def convert_char(char):
    
    if char == "a":
        new_char = "apa"
    return new_char







def p_sentence(sentence):
    new_sentence=""
    for char in sentence:    
        new_sentence += convert_char(char)
    return "Bapasipicopo"
