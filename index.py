from funcs.lesson_2 import  gess_carachter 
from funcs.lesson_3 import  game_screen 
from funcs.lesson_4 import  get_char_and_filter
from funcs.lesson_5  import is_valid_input 
from funcs.lesson_6 import  try_update_letter_guessed 
from funcs.lesson_7 import  show_hidden_word 
from funcs.lesson_8 import  print_hangman 
from funcs.lesson_8 import  HANGMAN_PHOTOS 
from funcs.lesson_9 import  choose_word 
from funcs.multi_line_screen import display_multiline_text 
from funcs.multi_line_screen import list_to_print
from funcs.opening_screen    import display_opening_screen
from funcs.lesson_8          import HANGMAN_PHOTOS
from  funcs.update           import process_failed_or_succeededs
from  funcs.find_winner      import player_won 





import string

def main():
  
  # opening  actions
  opening_sentence  = [ 'Welcome' , 'to' , 'The' , 'Game' , 'Hangman' , '!!!']
  opening_sentence_1 = [ 'The' , 'Game' , 'From' , '1990' ]
  display_multiline_text(list_to_print , delay=0.3)
  display_opening_screen( opening_sentence)
  display_opening_screen( opening_sentence_1 )
    
   
  file_path = input("Please enter the path to the word file: ")
  index     = input("Please enter the index for the word: ")
  print("\n")
  print("\n")
  print("\n")
    

  index = int(index)
  all_secret_word , secret_word  = choose_word(file_path, index)  
  
  guessed_letters   = []
  incorrect_guesses = 0
  max_attempts      = 7
# 

    
  while incorrect_guesses < max_attempts:
        
       
        print_hangman(incorrect_guesses) 
        print( show_hidden_word(secret_word , guessed_letters ) )
        print("\n\n")
        guess = input("Enter a single letter: ").lower()
        print("\n")
        print("\n")
        print("\n")
    
    
        # if  is_valid_input(guess) == False :
        #     print("Please insert a letter only !!!")
        #     continue
        # else:
        #         if guess in secret_word[:-1]:
        #            guessed_letters.append(guess)
        #            continue 
        #         else:
        #              print()
                     
        #              incorrect_guesses +=1   


        error_or_success , num  , bool_ =   process_failed_or_succeededs(guess ,  secret_word  , guessed_letters )
        if incorrect_guesses == 6 :
                  print("You lose The Game !!! ")
                  print("\n\n\n" )
                  break
        if error_or_success == 'E' and  num == 1:
            print("Please Insert Only letters !!! ")
            continue 
        if error_or_success == 'E' and  num == 2:
            print("Please ensure that the Secret word is  non-empty  .!!! ")
            break
        if error_or_success == 'E' and  num == 3:
            print("Please ensure that third argument is type of list !!! ")
            break 
        if error_or_success == 'S' and  num == 10 and bool_ == False :
              print("X\n")
              string_list = " -> ".join(guessed_letters)
              print(string_list) 
              incorrect_guesses +=1
        if  error_or_success == 'S' and num == 13 and bool_ == False:
             print("X\n")
             string_list = " -> ".join(guessed_letters)
             print(string_list) 
             incorrect_guesses +=1        

        if error_or_success == 'S' and  num == 100  and bool_ == True : 
            guessed_letters.append(guess);
            print("Nice answer !!!\n")
            print(guess)
        if player_won(secret_word , guessed_letters ):
                win_mess = [ 'Congratulations' , 'you' , 'won' , 'the' , 'game',  '!!!']
                print( "\n" * 4 )
                display_opening_screen( win_mess )
                print( "\n" * 4 )
                display_opening_screen(secret_word)
                print( "\n" * 4  )
                break
            
                  








if __name__ == "__main__":
    main()



