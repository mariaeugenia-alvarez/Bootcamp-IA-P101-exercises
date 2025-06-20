def convert_char(char, consonant):
    new_char = char
    vowel = "aeiou"
    for v in vowel:
        if v == char:
            new_char = v + consonant + v
            break
    return new_char


def p_sentence(sentence, consonant):
    new_sentence = ""
    for letter in sentence:
        new_sentence += convert_char(letter, consonant)
    return new_sentence
