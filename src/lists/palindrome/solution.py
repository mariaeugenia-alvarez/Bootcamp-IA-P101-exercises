def solution(word: str):
    # confirma si una palabra es palíndroma
    result = False
    i = 0
    j = -1
    word = word.lower()
    while i < ((len(word)) // 2):
        if word[i] == word[j]:
            i += 1
            j -= 1
            result = True
        else:
            result = False
            break
    return result
