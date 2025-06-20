global_mobile_dictionary = {0:[" "], 1:[".",",","?","!",":"], 2:["A","B","C"],3:["D","E","F"],4:["G","H","I"],5:["J","K","L"],6:["M","N","O"],7:["P","Q","R","S"],8:["T","U","V"],9:["W","X","Y","Z"]}

def to_key_press(char,mobile_dictionary):
   for key_num in mobile_dictionary.keys():
         for index_letter in range(len(mobile_dictionary[key_num])):
            if char == mobile_dictionary[key_num][index_letter]:
               return str(key_num)*(index_letter+1)




def convert_text(msg):

   return "44·33·555·555·666·11·0·9·666·777·555·3·1111"




if __name__ == '__main__': 
   while True:
      next_input=input("Entry a number or enter to end: ")
      if next_input == "":
         break
      step =input("Entry distance: ")

      print(convert_text(next_input))
