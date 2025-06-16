def get_invoice(nlist: list):
        tickets= [["Baby",0,0],["Children",14,0],["Adult",23,0]]
        tickets = number_tickets(tickets,nlist)
        pbaby, pchildren, padult, total = get_price(tickets)
        
        return format_output(tickets, pbaby, pchildren, padult, total)

def number_tickets(tickets,nlist):
   for i in nlist:  
      if i<=2:
         tickets[0][2]+=1
      elif 3<=i<=12:
         tickets[1][2]+=1
      elif 13<=i<65:
         tickets[2][2]+=1   
   return tickets

def get_price(tickets):
      pbaby = tickets[0][2] * tickets[0][1]
      pchildren = tickets[1][2] * tickets[1][1]
      padult = tickets[2][2] * tickets[2][1]
      total=pbaby+pchildren+padult
      return pbaby,pchildren,padult,total

def format_output(tickets, pbaby, pchildren, padult, total):
    txttotal = "El precio total es: {tot}. ".format(tot=total)
    txtbaby = "{txt}: {ntickets} = {price}. ".format(ntickets=tickets[0][2],price=pbaby,txt=tickets[0][0])
    txtchildren = "{txt}: {ntickets} = {price}. ".format(ntickets=tickets[1][2],price=pchildren,txt=tickets[1][0])
    txtadult = "{txt}: {ntickets} = {price}. ".format(ntickets=tickets[2][2],price=padult,txt=tickets[2][0])
    
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
