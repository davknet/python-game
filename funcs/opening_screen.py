
import string
import time


text_list = ["Welcome", "to", "the", "Hangman", "Game!"]
    
    # for word in text_list:
    #     print(word, end=" ", flush=True)  # Print words with space, stay on the same line
    #     time.sleep(1)  # Pause for 1 second


def display_opening_screen(list_of):
    """ 
    
    """
    text = list_of
    for letter in text:
        print(letter, end=" ", flush=True)
        time.sleep(0.3)
    print()  # Move to new line after full text is displayed



def main():

#    display_opening_screen(list_to_print)

 if __name__ == "__main__":
    main()