def convert_char(char,consonant):
    new_char = char
    vowel = "aeiou"
    for i in range(len(vowel)):
      if char == vowel[i]:
         new_char = vowel[i] + consonant + vowel[i]
         break
    return new_char


def p_sentence(sentence,consonant):
    new_sentence=""
    for letter in sentence:    
        new_sentence += convert_char(letter,consonant)
    return new_sentence
