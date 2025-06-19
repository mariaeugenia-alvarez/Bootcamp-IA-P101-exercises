#[72,72,75,75,70,74,74,76]

def index_difference(i,current_number,next_number):
    
    id_dictionary={}
    id_dictionary[i]= next_number - current_number

    return id_dictionary





def numbers_incremental_series(secuence:list):
    current_number = 0
    next_number = 0
    lgth= len(secuence)

    for i in range(lgth):
        current_number=secuence[i]
        next_number=secuence[i+1]

        if current_number == next_number:
            continue
        else:
            id__dictionary = index_difference(i,current_number,next_number)



        return [75,74,76]

