
from funcs.lesson_5  import is_valid_input








def process_failed_or_succeededs( letter , secret_word ,  old_letters_gessed    ):
    """ The function receives three parameters.
      The first parameter is a letter that the user tries to guess.
      The second parameter is a list of the letters that were guessed,
      and the third parameter is a word that the user must guess.
      The function makes all the game's logic and returns in different 
      situations with different values as tuple; the function doesn't 
      validate arguments, so you must ensure that all marameters are valid 
      :param letter: The English letter 
      :type letter: str 
      :param secret_word: word string 
      :type param: str
      :param old_letters_gessed: list of english letters that were guessed 
      :type old_letters_gessed: list 
      :return  three variables deferent types 
      :rtype tuple 
    """

    # sorry i have to validate othervise  the logic will  be very large 
    if not is_valid_input(letter):
        return ('E' , 1  , False )
    if not isinstance(secret_word , str ) or len( secret_word ) == 0 :
        return ('E' ,  2 , False )
    if not isinstance( old_letters_gessed , list  ):
        return ('E' , 3 , False )
    if letter in old_letters_gessed :
        return ('S' , 10  , False  )
    if len( secret_word ) == len(old_letters_gessed):
        return ('S' , 21  , True   )
    if not letter in secret_word :
       return ('S' , 13  , False  )   
    if letter in secret_word :
        return ('S' , 100  , True  )
    


def main():

 if __name__ == "__main__":
     main()       
