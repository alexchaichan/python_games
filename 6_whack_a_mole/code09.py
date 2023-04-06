# dont know why but on my keyboard i have to press the buttons really hard / multiple times .... :D

# import libraries
from psychopy import core, event,    visual
import random

#create variables
ROUNDS = 20
esc=['escape']
hit=["left", "down", "right"]
# creat some moles
i_moles = range(3)


game_over = False

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

print_start_text = visual.TextStim(win, "Hey, have fun while playing my whack a mole game \n press: \n left arrow to hit the left mole \n down arrow to hit the middle mole \n right arrow to hit the right mole \n esc for quit the game \n any key to start!", color=(0,1,0), bold = True, ) #exit text
print_start_text.draw()
win.flip()
event.waitKeys()

while game_over == False:
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
            key = event.waitKeys(BLANK, keyList=esc+hit) 

                
            #presentation
            mole.draw()
            key = event.waitKeys(PRESENT, keyList=esc+hit)
            
            # test for key press
            press_key_text = visual.TextStim(win, key, color=(0,1,0), bold = True, ) #exit text
            press_key_text.draw()
            
                

            if key:
                if key[0]==hit[0]:
                    
                    mole = visual.Circle(win, pos=(LOCATION[0],0), radius=75, edges=32, units='pix', lineColor='black', fillColor='white')
                    mole.draw()
                    core.wait(0.4)
                elif key[0]==hit[1]:
                    mole = visual.Circle(win, pos=(LOCATION[1],0), radius=75, edges=32, units='pix', lineColor='black', fillColor='white')
                    mole.draw()
                    core.wait(0.4)
                elif key[0]==hit[2]:
                    mole = visual.Circle(win, pos=(LOCATION[2],0), radius=75, edges=32, units='pix', lineColor='black', fillColor='white')
                    mole.draw()
                    core.wait(0.4)
        if key:
            if key[0]==esc[0]:
                game_over= True
                break

win.close()


