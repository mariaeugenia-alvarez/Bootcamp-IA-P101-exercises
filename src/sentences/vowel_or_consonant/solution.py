def solution(entry):

    if entry in "aeiou":
        result = "vowel"
    elif entry == "y":
        result = "ambiguous"
    else:
        result = "consonant"
    return result
