def get_invoice(age: list):
        nbaby=0
        nchildren=0
        nadult=0
        pbaby=0
        pchildren=0
        padult=0
        casebaby="Niños de 2 años o menos"
        casechildren="Niños de 3 a 12 años"
        caseadult="Niños de 13 a 65 años"
          
        for i in age:
                if i<=2:
                   nbaby+=1
                   pbaby=nbaby*0
                elif 3<=i<=12:
                   nchildren+=1
                   pchildren+=nchildren*14
                elif 13<=i<65:
                   nadult+=1
                   padult+=nadult*23             
                   
        total=pbaby+pchildren+padult
        txttotal = "El precio total es: {tot}. ".format(tot=total)
        txtbaby = "{txt}: {ntickets} = {price}. ".format(ntickets=nbaby,price=pbaby,txt=casebaby)
        txtchildren = "{txt}: {ntickets} = {price}. ".format(ntickets=nchildren,price=pchildren,txt=casechildren)
        txtadult = "{txt}: {ntickets} = {price}. ".format(ntickets=nadult,price=padult,txt=caseadult)

        return txttotal + txtbaby + txtchildren + txtadult

def is_finish_input(next_input):
    return next_input == ""

def is_not_valid_input(next_input):
   result = True
   digits = list("0123456789")
   for char in next_input:
      if char in digits:
         result = False
         break
      return result
    
if __name__ == '__main__': 
   nlist=[]
   while True:
      next_input=input("Entry a number or enter to end: ")
      
      if is_finish_input(next_input):
         break
      
      if is_not_valid_input(next_input):
         print("Esto no es un número")

      else:
         age = int(next_input)
         nlist.append(age)


   print(get_invoice(nlist))
