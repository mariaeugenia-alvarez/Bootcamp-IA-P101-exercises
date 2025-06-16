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

def to_string(numbers_list):
   return []


def transpose(literal,step):
      
      literal_list=list(literal)
      number_list = to_numbers(literal_list, dictionary=global_dictionary)
      #cifrar
      string_list = to_string(number_list)

      return ("bki bci")
