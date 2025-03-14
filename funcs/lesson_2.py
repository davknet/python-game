def gess_carachter(letter):
    """ The function receives a parameter string that 
    contains one character and returns it for printing
    :param letter: carachter 
    :type  letter: str
    :return  carachter 
    :rtype  str 
    """
    if not isinstance(letter , str ) or len(letter) == 0:
        print("Please Provided Input must be non-emtpy string and must contain only one carchter!!!")
        return ''
    return letter 

def main():
    print(gess_carachter(input("Please Gess a letter !!!: ")))

if __name__ == "__main__":
    main()    

