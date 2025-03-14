


def show_hidden_word(secret_word, old_letters_guessed):
    """ The function receives two parameters. The first parameter is 
      the secret word, which is the word that must be guessed,
      and the second parameter is the old letter guessed  
      the list of letters from secret word that was already guessed ,
      The function returns a string with letters that were guessed from the 
      secret word and underscores for letters that were not 
      guessed  as one string there is  spaces between chars 
      :param secret_word  contains a word for  guessing 
      :type secret_word: str
      :param  old_letters_guessed: list of letters that ware guessed 
      :type old_letters_guessed:list of str 
      :return string letters that was guessed and the underscores for letters that ware not guessed
      :rtype  str  
    
    """

    if not isinstance(secret_word , str ) or len(secret_word) == 0:
        print("Please provide secret word as non-empty string !!! ")
        return ''
    elif not isinstance(old_letters_guessed , list ):
        print(" argument old_letters_guessed must be type of list  ")
        return ''
    
    new_secret_word = ''
    i = 0 
    for letter  in  secret_word  :
        if  letter  in  old_letters_guessed:
            new_secret_word +=' '+ letter
            i += 1 
        else:
             new_secret_word += ' _ '
             i += 1 
           
    return  new_secret_word  




def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))
  

if __name__ == "__main__":
     main()     


