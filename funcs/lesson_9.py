import os




def choose_word(file_path, index):
    """ The function receives two parameters: 
    the first is the file_path path to the file as a string,
      and the second is the index integer for the word's 
      location in the file. The function returns a tuple 
      that contains two variables. The first variable is the 
      number of unique words, and the  second is the
       word at the given position 
      :param  file_path: path for file 
      :type file_path: str 
      :param index: integer the location of the word 
      :return  to wariables  list of the unique  words and second index of the word 
      :rtype tuple 
    """
   
    if not isinstance(file_path , str ) or len(file_path) == 0 :
        print("The first argument must be non-emmpty string !!!")
        return ( 'error' ,)
    elif not os.path.exists(file_path):
        print("Please the first argument must link to the existing file !!!")
        return ('error', 'file doesn\'t exist')
    elif not isinstance(index , int ) or index < 0  :
        print("The  second argument must be type of integer and higher than 0 !!!   ")
        return('error', )

    with open(file_path , "r" , encoding='UTF-8') as words_dict: 
     string_of_words = words_dict.read()
    #  unique_word     = set( string_of_words.split())
     list_of_words    = list(string_of_words.split(" "))
     unique_words     = []
     for word in list_of_words:
         if not word in unique_words:
             unique_words.append(word)
      
     index = ( index - 1) % len(unique_words)
     return  len(unique_words) , unique_words[index] 
     
def main():
    words , word = choose_word("text_files/words.txt", 2 )
    print(words)
    print(word)
if __name__ == "__main__":
    main()        
