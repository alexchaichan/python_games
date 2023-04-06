# function to calculate the location of the card
def position_from_index(index):
    
    if index <= 3:
        x = -0.75+0.5*index
        y = 0.5
    else:
        x = -0.75+(-0.5)*-index -2
        y = -0.5
    
    return x, y