def convert_char(char):
    new_char = char
    vowel = "aeiou"
    for i in range(len(vowel)):
      if char == vowel[i]:
         new_char = vowel[i] + "p" + vowel[i]
         break
    return new_char


def p_sentence(sentence):
    new_sentence=""
    for letter in sentence:    
        new_sentence += convert_char(letter)
    return new_sentence
