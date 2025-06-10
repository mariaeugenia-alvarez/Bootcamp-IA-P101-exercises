def solution(profile,hour):

    if profile == "admin":
        return True
    elif profile == "usuario" and (8<=hour<=20):
        return True
    elif profile == "invitado" and (10<=hour<=16):
        return True
    else:
        return False
    


