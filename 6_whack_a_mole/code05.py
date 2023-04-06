# import libraries
from psychopy import visual, event
import random

#create variables
game_over = False
keyList=['escape']
COLOR = ['pink','red','yellow']
LOCATION = [-225,0,225]
rndm_mole = random.randrange(0,3)

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

# creat some moles
i_moles = range(3)


# start loop
while game_over == False:
    
    for x in i_moles:
        mole = visual.Circle(win, pos=(LOCATION[rndm_mole],0), radius=75, edges=32, units='pix', lineColor='black', fillColor=COLOR[rndm_mole])
        mole.draw()
    
    # lets flip it
    win.flip()
    
    
    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == keyList[0]:
            game_over = True