def get_invoice(age_list: list):
    tickets = [["Baby", 0, 0], ["Children", 14, 0], ["Adult", 23, 0]]
    tickets = number_tickets(tickets, age_list)
    pbaby, pchildren, padult, total = get_price(tickets)

    return format_output(tickets, pbaby, pchildren, padult, total)


def number_tickets(tickets, age_list):
    for i in age_list:
        if i <= 2:
            tickets[0][2] += 1
        elif 3 <= i <= 12:
            tickets[1][2] += 1
        elif 13 <= i < 65:
            tickets[2][2] += 1
    return tickets


def get_price(tickets):
    pbaby = tickets[0][2] * tickets[0][1]
    pchildren = tickets[1][2] * tickets[1][1]
    padult = tickets[2][2] * tickets[2][1]
    total = pbaby + pchildren + padult
    return pbaby, pchildren, padult, total


def format_output(tickets, pbaby, pchildren, padult, total):
    txttotal = f"El precio total es: {total}. "
    txtbaby = f"{tickets[0][0]}: {tickets[0][2]} = {pbaby}. "
    txtchildren = f"{tickets[1][0]}: {tickets[1][2]} = {pchildren}. "
    txtadult = f"{tickets[2][0]}: {tickets[2][2]} = {padult}. "
    return txttotal + txtbaby + txtchildren + txtadult


def is_finish_input(input_value):
    return input_value == ""


def is_not_valid_input(input_value):
    result = True
    digits = list("0123456789")
    for char in input_value:
        if char in digits:
            result = False
            break
        return result


if __name__ == "__main__":
    nlist = []
    while True:
        next_input = input("Entry a number or enter to end: ")

        if is_finish_input(next_input):
            break

        if is_not_valid_input(next_input):
            print("Esto no es un número")

        else:
            age = int(next_input)
            nlist.append(age)

    print(get_invoice(nlist))
