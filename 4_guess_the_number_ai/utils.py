def input_response(guess):
    
    # guessing part
    play = input('is it %s ?'% guess)


    # compute the winning scenario
    if play==str('='):
        print("got it!")
    # compute the greater scenario   
    elif play==str('>'):
        print('higher')
    # compute the lesser scenario
    elif play==str('<'):
        print('lower')
    # compute invalid input scenario
    else:
        print("Invalid input")
        
    return play

##########################################################################

def split_interval(lower_limit, upper_limit):
    
    #function: 
    
    # shrinks the range of upper and lower limit
    
    # parameters
    
    #lower : int
    #upper : int
    
    
    guess = (lower_limit + upper_limit) /2

    
    
    # returns 
    
    return int(guess) #:int 