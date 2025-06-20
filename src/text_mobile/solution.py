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


def to_key_press(char, mobile_dictionary):
    for key_num in mobile_dictionary.keys():
        for index_letter in range(len(mobile_dictionary[key_num])):
            if char == mobile_dictionary[key_num][index_letter]:
                return str(key_num) * (index_letter + 1)


def convert_text_to_number(msg):
    message = ""
    for letter in msg:
        letter_convert = to_key_press(letter, global_mobile_dictionary)
        message += letter_convert + "·"
    return message


def clean_to_list(msg):
    msg_list = []
    msg_list = msg.split("·")
    if msg_list[-1] == " ":
        msg_list.pop()
    return list(map(int, msg_list))


def convert_number_to_text(msg):
    msg_list_int = clean_to_list(msg)
    *****************************************
    letter_convert = to_key_press(letter, global_mobile_dictionary)
    message += letter_convert + "·"
    return message


if __name__ == "__main__":
    while True:
        next_input = input("Entry a message or entry a code: ")
        if next_input == "":
            break
        if int(next_input[0]) is True:
            print(convert_number_to_text(next_input))
        print(convert_text_to_number(next_input))
