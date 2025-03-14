





def player_won( secret_word , guessed_letter  ):
    """ The function receives two parameters. 
    The first parameter is a string secret word, and the second parameter is a list of letters.
      The function checks if the count of letters in the secret 
      word equals the count of the letters in the list
      of letters  and returns true or false 
      :param secret_word: word string
      :type secret_word: str
      :param guessed_letter: list of letters
      :type guessed_letter:list
      :return false or true 
      :rtype boolean

    """
    if  not isinstance(secret_word , str ) or len(secret_word) == 0 :
        print("The first parameter must be non-empty sting !!!")
        return False 
    if not isinstance(guessed_letter , list ):
        print("The Second parameter must be type of list !!!")
        return False 
    text_word = ''.join(sorted(set(secret_word )))
    list_word = ''.join( sorted(set(guessed_letter)))

    if  ( text_word == list_word  ) and (   len(list_word) == len(text_word) ):
        
        return  True 
    return False 


def main():
 
 
 if __name__ == "__main__":
    main()   



