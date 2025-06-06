
def solution(human_age):
    human_age = convert_to_float(human_age)

    if human_age<0:
        dog_age= "Error: edad negativa"
    elif human_age<=2:
        dog_age=human_age*10.5
    else:
        dog_age=2*10.5+(human_age-2)*4

    return dog_age

def convert_to_float(human_age):
    return float(human_age)


if __name__ == '__main__': 
    b=(input("enter your age: "))
    print(solution(b))
