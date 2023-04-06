# import libraries
from psychopy import core, event,    visual
import random

#create variables
ROUNDS = 4
esc=['escape']
# creat some moles
i_moles = range(3)

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

    
for a in range(ROUNDS):

    #randomized variables for every round
    COLOR = ['pink','red','yellow']
    LOCATION = [-225,0,225]
    RNDM_MOLE = random.randrange(0,3)




            
    #generating random parameters
    for x in i_moles:
        mole = visual.Circle(win, pos=(LOCATION[RNDM_MOLE],0), radius=75, edges=32, units='pix', lineColor='black', fillColor=COLOR[RNDM_MOLE])
            
        #generate random interval for moles
        BLANK = random.uniform(0.5,1.5)
        PRESENT = random.uniform(0.25,0.5) 
            
            
            
        #blank
        win.flip()
        key = event.waitKeys(BLANK, keyList=esc) 

            
        #presentation
        mole.draw()
        key = event.waitKeys(PRESENT, keyList=esc)#better to rename the second variable (otherwise we have two times variable "key"??
            
    
        if key:
            if key[0]:
                win.close()
