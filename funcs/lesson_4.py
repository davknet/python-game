
def get_char_and_filter(letter):
    """ The function receives a parameter string, fits it,
    and if there is more than one character, 
    returns E1; if there is a simbole, returns E2;
    if there is no English letter, returns E3
    :param letter:  string must be one character 
    :type  leter : str 
    :return  character 
    :rtype str 
    """
    simbols = ['!' , '@' , '#' , '$' , '%' , '^' , '&' , '*' , '(' ,')' , '_' , '-' , '=', '+' , '?' , 
               '~' , '±' , '>' , '<' , '|' , '\\' , '"' , '/' , ' ']
    english_leters_sm = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    english_leters_lg = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                          'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']



    if not isinstance(letter , str ) or len(letter) == 0  or len(letter) > 1 :
        return 'E1'
    elif letter in simbols :
        return 'E2'
    elif  not letter in  english_leters_sm and not letter in english_leters_lg:
        return 'E3'
    else:
        return letter.lower()
    
def  main():
     print("==================== \n")
     print("==================== \n")
     print("\n\n")
     lett_ = get_char_and_filter(input("Please Insert A letter : "))

     if lett_ == 'E1':
          print("\n")
          print("Error: Please Insert non-empty string !!!")
     elif  lett_ == 'E2':
         print("\n")
         print("Please insert letter that   doesn't  contain any simbole !!! ")
     elif lett_ == 'E3':
         print("\n")
         print("Error: Please insert only an English letter !!! ")

     else:
         print("\n\n")
         print(lett_)    
             

     print("\n\n")
     print("==================== \n")
     print("==================== \n")
if __name__ == "__main__":
    main()     

    
    

   
