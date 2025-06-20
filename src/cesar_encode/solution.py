global_dictionary = list("abcdefghijklmnñopqrstuvwxyz")


def to_numbers(literal_list, dictionary):
    number_list = []
    for word in literal_list:
        if word in dictionary:
            number = dictionary.index(word)
        else:
            number = word
        number_list.append(number)
    return number_list


def to_string(numbers_list, dictionary):
    chain = ""
    for number in numbers_list:
        if isinstance(number, int):
            char = dictionary[number]
        else:
            char = number
        chain += char

    return chain


def encrypt(number_list, shift, dictionary):
    encrypt_number_list = []
    length = len(dictionary)
    for number in number_list:
        if isinstance(number, int) is False:
            encrypt_number = number
        else:
            encrypt_number = (number + shift) % length
        encrypt_number_list.append(encrypt_number)
    return encrypt_number_list


def transpose(literal, shift_step):
    literal_list = list(literal)
    number_list = to_numbers(literal_list, global_dictionary)
    encrypt_list = encrypt(number_list, shift_step, global_dictionary)
    return to_string(encrypt_list, global_dictionary)


if __name__ == "__main__":
    while True:
        next_input = input("Entry a number or enter to end: ")
        if next_input == "":
            break
        step = input("Entry distance: ")

        print(transpose(next_input, int(step)))
