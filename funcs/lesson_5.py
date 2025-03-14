#
# 
def is_valid_input(letter_guessed):
    """ The function receives a parameter letter; it checks if 
    the parameter is correct and does not contain symbols or more 
    than one letter and returns true or false 
    :param letter_guessed: letter 
    :type letter_guessed:str
    :return true or false 
    :rtype boolean 
    """
    if not isinstance( letter_guessed , str ) or len(letter_guessed) == 0  :
        print("problem in str or length" + letter_guessed )
        return False 
    elif  not letter_guessed.isalpha():
        print("problem with english " + letter_guessed )
        return False 
    else:
        return True  
    


def main():
     
     print(is_valid_input(input("Please insert a Letter :")))

if __name__ == "__main__":
    main()      
    
 