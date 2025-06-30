abecedario = "abcdefghijklmnñopqrstuvwxyz"


def to_cesar(car, d, abc):
    new_car = car
    if car in abc:
        pos = abc.index(car)
        new_pos = (pos + d) % len(abc)
        new_car = abc[new_pos]
    return new_car


def createCesar(car, abc):
    return to_cesar(car, 2, abc)


def cesar(cadena, fx):
    result = ""
    for car in cadena:
        result += fx(car, abecedario)
    return result


def cifrar(cadena):
    return cesar(cadena, createCesar)


if __name__ == "__main__":
    while True:
        next_input = input("Entry a number or enter to end: ")
        if next_input == "":
            break

        print(cifrar(next_input))
