
def game_screen(word):
    """ The function receives a parameter that contains only 
    one word, no space. It calculates the length of the word and prints 
    the same count of underscore character
    :param word: string no white space 
    :type param: str 
    :return  count of underscrore 
    :rtype str 
    """
    if not isinstance(word ,str ) or len(word) == 0 or " " in word :
        print("Please provide paramter non-empty string that doesn't contain empty space !!!")
        return "error"
    return len(word) * " _ "


def main():
   print(game_screen(input("Please insert a word : ")))
   print("\n")
if __name__ == "__main__":
    main()     