# import libraries
from psychopy import visual, event

# create some varialbe 
game_over = False 
keyList=['escape']



# creating a 800 x 600 window
win = visual.Window(size=(800, 600))

while game_over == False:
    
    keys = event.getKeys()
    if keys:
        # q quits the experiment
        if keys[0] == keyList[0]:
            game_over = True



