from funcs.lesson_5  import is_valid_input 


def try_update_letter_guessed(letter_guessed, old_letters_guessed , ):
    """  The function receives two parameters.
    The first parameter is a letter that has been guessed,
     and the second parameter is a list of letters that was guessed.
     If the first parameter letter is guessed,
     the function adds it to the second parameter list of old letters guessed 
     and returns True; if the letter is not guessed, the function prints X,
     a capital letter, and ander it prints list of old guessed letter 
     as string seperated by arrow and returns False 
    :param  letter_guessed: letter 
    :type  letter_guessed: str 
    :param old_letters_guessed: list of letters 
    :type old_letters_guessed: lits of strings 
    :return  true or false 
    :rtype boolean 
    """
    new_old_guessed_letter_list = sorted( old_letters_guessed , key=lambda x:( x.islower() , x) )
    letter_to_guess = [ 'H', 'e' , 'l' , 'l' , 'o' , 'W' , 'o' , 'r' , 'l' , 'd']
    if not is_valid_input(letter_guessed ):
        print("X\n")
        return False 
    elif letter_guessed in old_letters_guessed:
         print("X\n")
         string_list = " -> ".join(new_old_guessed_letter_list)
         print(string_list) 
         return False 
     
    elif  not letter_guessed in letter_to_guess:
       print("X\n")
       string_list = " -> ".join(new_old_guessed_letter_list)
       print(string_list) 
       return False 
    else:
         old_letters_guessed.append(letter_guessed)   
         return True 

    return True 
    


def main():
    old_letters_guessed = [ 'e' , 'l' , 'r' ]
    get_answer = try_update_letter_guessed(input("Please Insert a Letter : "), old_letters_guessed )
    print("\n\n")
    print(get_answer)
if __name__ == "__main__":
    main()    