global_mobile_dictionary = {
    0: [" "],
    1: [".", ",", "?", "!", ":"],
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"],
}


def to_key_press_text(char, mobile_dictionary):
    for key_num in mobile_dictionary.keys():
        for index_letter in range(len(mobile_dictionary[key_num])):
            if char == mobile_dictionary[key_num][index_letter]:
                return str(key_num) * (index_letter + 1)


def to_key_press_number(digit, mobile_dictionary):
    for key_num in mobile_dictionary.keys():
        if int(digit[0]) == key_num:
            return mobile_dictionary[key_num][len(digit) - 1]
    return ""


def convert_text_to_number(msg):
    message = ""
    for letter in msg:
        letter_convert_text = to_key_press_text(letter, global_mobile_dictionary)
        message += letter_convert_text + "·"
    return message


def clean_to_list(msg):
    msg_list = []
    msg_list = msg.split("·")
    if msg_list[-1] == "":
        msg_list.pop()
    return msg_list


def convert_number_to_text(msg):
    message = ""
    msg_list = clean_to_list(msg)  # lista de números
    for number in msg_list:
        letter_convert_number = to_key_press_number(number, global_mobile_dictionary)
        message += letter_convert_number
    return message


if __name__ == "__main__":
    MODE = ""

    while True:
        option = input(
            "\033[93mElige una de las funciones:\n1-Texto\n2-Código\033[0m\n"
        )
        if option == "1" or option == "2":
            MODE = option
            break

    while True:
        next_input = input("Introduce la cadena: ")
        if next_input == "":
            break
        if MODE == "2":
            print(convert_number_to_text(next_input))
        else:
            print(convert_text_to_number(next_input.upper()))
