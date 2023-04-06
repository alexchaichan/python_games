# import libraries
from psychopy import core, event, visual
import random

#create variables
# constants
COLOR = ['pink','red','yellow']
LOCATION = [-225,0,225]
RNDM_MOLE = random.randrange(0,3)


# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

# creat some moles
i_moles = range(3)

# start loop
    
#generating random parameters
for x in i_moles:
    mole = visual.Circle(win, pos=(LOCATION[RNDM_MOLE],0), radius=75, edges=32, units='pix', lineColor='black', fillColor=COLOR[RNDM_MOLE])
    
#for y in range(0):
    BLANK = random.uniform(0.5,1.5)
    PRESENT = random.uniform(0.5,0.75) 
    
    
    
    #blank
    win.flip()
    core.wait(BLANK)
    
    #presentation
    

    mole.draw()
    core.wait(PRESENT)
    
    # end the game with esc
    #keys = event.getKeys()
    #if keys:
    #    # define the keylist
    #    if keys[0] == keyList[0]:
    #        game_over = True
win.close