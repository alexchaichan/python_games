# import libraries
from psychopy import visual, event

#create variables
game_over = False
keyList=['escape']

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

# start loop
while game_over == False:
    

    # lets flip it
    win.flip()
    
    
    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == keyList[0]:
            game_over = True