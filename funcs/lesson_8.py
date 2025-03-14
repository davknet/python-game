from funcs.lesson_1 import hangman_stages

HANGMAN_PHOTOS = { 
     '0'  : hangman_stages[0] , 
     '1'  : hangman_stages[1] , 
     '2'  : hangman_stages[2] , 
     '3'  : hangman_stages[3] , 
     '4'  : hangman_stages[4] , 
     '5'  : hangman_stages[5] ,
     '6'  : hangman_stages[5] 
     }



def print_hangman(num_of_tries):
    """Prints the Hangman state based on the number of tries.

    This function receives the number of failed attempts and prints the 
    corresponding Hangman drawing.

    :param num_of_tries: The number of incorrect attempts made.
    :type num_of_tries: int
    :return: None void doesn't return anything 
    :rtype : None
    """
    global HANGMAN_PHOTOS

    if not isinstance( num_of_tries , int ) or num_of_tries < 0 :
           print("Please provide number_of tries integer between 0 and 7 !!!")
           return 
    elif num_of_tries > 6 :
           
           print(" Number_of tries can't be higher than 6 !!! ")
           return 
    print(HANGMAN_PHOTOS[str(num_of_tries)])

def main():

      print_hangman(1)

if __name__ == "__main__":
      main()
