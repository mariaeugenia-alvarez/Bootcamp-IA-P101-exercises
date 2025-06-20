def solution(n: list):
    # calcula la media de los valores de una lista
    result = 0
    i = 0
    if n == []:
        result_average = 0
    else:
        while i < len(n):
            result += n[i]
            i += 1
        result_average = result / len(n)
    return result_average
