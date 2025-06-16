def get_invoice(age: list):
        
        tickets= [["Baby",0,0],["Children",14,0],["Adult",23,0]]
        pbaby=0
        pchildren=0
        padult=0
        casebaby="Niños de 2 años o menos"
        casechildren="Niños de 3 a 12 años"
        caseadult="Niños de 13 a 65 años"
                   
        pbaby, pchildren, padult, total = get_price(tickets,age)
        return format_output(tickets[0][2], tickets[1][2], tickets[2][2], pbaby, pchildren, padult, total, casebaby, casechildren, caseadult)

def get_price(tickets,age):
   for i in age:  
      if i<=2:
         tickets[0][2]+=1
      elif 3<=i<=12:
         tickets[1][2]+=1
      elif 13<=i<65:
         tickets[2][2]+=1   

   pbaby = tickets[0][2] * tickets[0][1]
   pchildren = tickets[1][2] * tickets[1][1]
   padult = tickets[2][2] * tickets[2][1]
   total=pbaby+pchildren+padult
   return pbaby,pchildren,padult,total

def format_output(nbaby, nchildren, nadult, pbaby, pchildren, padult, total, casebaby, casechildren, caseadult):
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
