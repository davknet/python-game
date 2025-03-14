import time 
import string 

list_to_print = [
     r"""   
    _    _
   | |  | |
   | |__| |   
   |  __  |   
   | |  | |   
   |_|  |_| 
   
   
             """  
        , 

 r"""  
        
           
    __ _ 
   / _' | 
  | (_| | 
     \__,_| 
     
     
            """ 
        ,   

     r"""


     _ __
    |  _ \ 
    | | \ |
    |_| |_| 
    
             """ 
    
    ,   

    r"""
     

         ____
    / __  \ 
   | | _| |
   \____ |
                             __/ | 
                  |____/  """  ,


    r"""
 
     
      __  __  __
   |   _     _   \
    |  |  |  |  | |
    |_ |  |_ |  |_|
    
      """ 
      
      
      ,




     r"""  
        
           
           __ _ 
     / _' | 
    | (_| | 
     \__,_| 
     
     
            """ 
        ,   





     r"""


     _ __
    |  _  \ 
    | | \ |
    |_| |_| 
    
             """ 
    
    


]


def display_multiline_text(text_list, delay=1):
    """  The function receives two parameters. 
    The first is a list of multiline strings, 
    and the second is a numeric integer or float function that prints all 
    multi line strings by the sequens with time delay of givan second marameter 
    :param text_list: list of multi line strings 
    :type text_list: list 
    :param delay: nnumeric integer or float 
    :type  delay: float or integer 
    :return void 
    :rtype None 
    """

    if not isinstance(text_list , list  ) or len(text_list) == 0 :
       print(" Please provide parameter one list of multiline string !!! ")
       return
    if not isinstance(delay , int ) and not isinstance( delay ,  float ):
      print(" Please provide parameter two  numeric float or integer  !!! ")
      return 
    
    # creates list of stings by line 
    split_lines = [block.split("\n") for block in text_list]
    
    # get maximum lines 
    max_lines = max(len(lines) for lines in split_lines)
   
    
    for lines in split_lines:
        while len(lines) < max_lines:
            lines.append("" * len(lines[0]))  
    

    for i in range(max_lines):
        for block in split_lines:
            print(block[i], end=" ") 
        print()  
        time.sleep(delay)  




def main():
#    display_multiline_text(list_to_print , delay=0.2)   
 if __name__ == "__main__":
    main()     