def es_par(n):
    return n % 2 == 0


def partition_list(number_list, es_par):
    even_list = []
    not_even_list = []
    result = {}
    for number in number_list:
        if es_par(number):
            even_list.append(number)
        else:
            not_even_list.append(number)

    result = {"pasan": even_list, "no pasan": not_even_list}
    return result
