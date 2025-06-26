abecedario = "abcdefghijklmnñopqrstuvwxyz"


def to_cesar(car, d, abc):
    new_car = car
    if car in abc:
        pos = abc.index(car)
        new_pos = (pos + d) % len(abc)
        new_car = abc[new_pos]
    return new_car


def cesar(cadena, d, abc=abecedario):
    result = ""
    for car in cadena:
        result += to_cesar(car, d, abc)
    return result


if __name__ == "__main__":
    while True:
        next_input = input("Entry a number or enter to end: ")
        if next_input == "":
            break
        d = int(input("Entry distance: "))

        print(cesar(next_input, d))
