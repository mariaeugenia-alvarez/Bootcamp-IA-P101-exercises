def index_difference(i, current_number, next_number):
    index = i + 1
    id_dictionary = {}
    id_dictionary[index] = next_number - current_number

    return id_dictionary


def changes_in_list(secuence, lgth, id_acumm_dictionary):
    for i in range(lgth - 1):
        current_number = secuence[i]
        next_number = secuence[i + 1]

        if current_number != next_number:
            id_dictionary = index_difference(i, current_number, next_number)
            id_acumm_dictionary.update(id_dictionary)


def filter_increasing_numbers(secuence, id_acumm_dictionary, series_list):
    for index in id_acumm_dictionary.keys():
        if id_acumm_dictionary[index] >= 0:
            series_list.append(secuence[index])


def numbers_incremental_series(secuence: list):
    lgth = len(secuence)
    id_acumm_dictionary = {}
    series_list = []

    if lgth == 0:
        return series_list

    changes_in_list(secuence, lgth, id_acumm_dictionary)

    filter_increasing_numbers(secuence, id_acumm_dictionary, series_list)

    return series_list
