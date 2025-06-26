def generate_invoice(age_list, generate_get_price):
    result = 0
    for age in age_list:
        result += generate_get_price()(age)
    return result
