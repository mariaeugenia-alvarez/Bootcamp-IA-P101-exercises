def solution(profile, hour):

    if profile == "admin":
        return True
    if profile == "usuario" and (8 <= hour <= 20):
        return True
    if profile == "invitado" and (10 <= hour <= 16):
        return True

    return False
