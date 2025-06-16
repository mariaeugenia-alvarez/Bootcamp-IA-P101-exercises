global_dictionary = list("abcdefghijklmnñopqrstuvwxyz")

def to_numbers(literal_list, dictionary):
   number_list=[]
   for word in literal_list:
      if word in dictionary:
         number = dictionary.index(word)
      else:
         number = word
      number_list.append(number)
   return number_list

def to_string(numbers_list, dictionary):
   chain=""
   for number in numbers_list: 
      if isinstance(number,int):
         char=dictionary[number]
      else:
         char=number
      chain+=char

   return chain


def transpose(literal,step):
      
      literal_list=list(literal)
      number_list = to_numbers(literal_list, global_dictionary)
      #cifrar

      return  to_string(number_list, global_dictionary)
