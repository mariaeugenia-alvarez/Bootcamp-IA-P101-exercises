def solution(n: list):
    # calcula la suma de los valores de una lista
    result = 0
    i = 0
    while i < len(n):
        result += n[i]
        i += 1
    return result
