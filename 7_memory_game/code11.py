# import libraries
import os
from psychopy import core, event, visual
import random
#import utils # it was not possible to import them from utils

# create some functions
# function to calculate the location of the card
def position_from_index(i_chicken):
    
    if i_chicken <= 3:
        x = -0.75+0.5*i_chicken
        y = 0.5
    else:
        x = -0.75+(-0.5)*-i_chicken -2
        y = -0.5
    
    return x, y

##################################################################################

# create a window
win = visual.Window(size=(960, 800), units='norm')
mouse = event.Mouse(visible=True, win=win)

## creating some variables

# game state game run while 'running'
game_state = 'running'
#implement esc key
esc=['escape']

# creat index for chickens
i_chicken = range(0,8)
#extract the single files inside the directory
image=[x for x in os.listdir("images/chicken")*2 if x.startswith('l')]
#shuffle the pictures
image = random.sample(image, 8)

while game_state == 'running':

    
    
# create cards 
    for card in i_chicken:
        
        
        
        # create the path for each chicken picture
        path = os.path.join("images", "chicken", image[card]) 
        
        card = {
        'front' : visual.ImageStim(win, image=path, size=(0.5, 1), units='norm', pos=(position_from_index(card))),
        'back' : visual.Rect(win, units='norm',size=(0.5,1), pos=(position_from_index(card)), lineColor='white', fillColor='cyan'),
        'side' : None,
        'show' : True
        }
        # update the card
        card['side'] = card['back']
        
        buttons = mouse.getPressed()
        
        if buttons: # if the left mouse button is pressed
            if buttons[0]==1:
                core.wait(0.5)
                card['side'] = card['front']
                
        # draw the obejcts
        card['side'].draw()
        
    # flip to view the image
    win.flip()
    
    # wait for keypress to abort


        # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == esc[0]:
            game_state = 'off'


# close the window after keypress
