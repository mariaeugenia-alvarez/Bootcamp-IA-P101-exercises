def solution(chars:list):
        #suma todos los caracteres de las palabras de una lista
        result=0
        i=0
        if chars==[]:
                result= 0
        else:
                while i < len(chars):
                        result+=len(chars[i])
                        i+=1
        return result




