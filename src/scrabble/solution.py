global_scrabble_dictionary = {
    "A": 1,
    "E": 1,
    "O": 1,
    "S": 1,
    "I": 1,
    "U": 1,
    "N": 1,
    "L": 1,
    "R": 1,
    "T": 1,
    "C": 3,
    "D": 2,
    "M": 3,
    "B": 3,
    "P": 3,
    "H": 4,
    "G": 2,
    "Y": 4,
    "Q": 5,
    "J": 8,
    "Ñ": 8,
    "X": 8,
    "Z": 10,
    "LL": 8,
    "RR": 8,
    "CH": 5,
}


def substring(str, target):
    return str.count(target)


def remove(str, target):
    return str.replace(target, "")


def get_sorted_keys(scrabble_dictionary):
    return sorted(scrabble_dictionary.keys(), key=lambda k: len(k), reverse=True)


def get_points(n_letters, key, scrabble_dictionary):
    return n_letters * scrabble_dictionary[key]


def score(word, scrabble_dictionary):
    n_letters = 0
    total_points = 0
    new_word = word
    my_dict = {}
    for key in get_sorted_keys(scrabble_dictionary):
        n_letters = substring(new_word, key)
        if n_letters != 0:
            point = get_points(n_letters, key, scrabble_dictionary)
            total_points += point
            my_dict.update({key: n_letters})
            new_word = remove(new_word, key)
        else:
            continue
    return total_points, my_dict


if __name__ == "__main__":

    while True:
        next_input = input("Intro your word!!\n").upper()
        if next_input == "":
            break
        print(
            "La puntuación y cantidades de la palabra son: ",
            score(next_input, global_scrabble_dictionary),
        )
