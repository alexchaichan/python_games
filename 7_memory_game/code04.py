# import libraries
from psychopy import core, event, visual
#import utils # it was not possible to import them from utils

# create some functions
# function to calculate the location of the card
def position_from_index(index):
    x = -0.75+(-0.25)*index
    y = 0.5
    
    return x, y
    
############################################################



# create a window
win = visual.Window(size=(960, 800), units='norm')

i_chicken = [0, -2, -4, -6]

# create the chicken
chicken = visual.ImageStim(win, image="images/chicken/r01.png", size=(0.5, 1), units='norm', pos=(position_from_index(i_chicken[0])))

# create the backside of the card
backside = visual.Rect(win, units='norm',size=(0.5,1), pos=(position_from_index(i_chicken[0])), lineColor='white', fillColor='black')



# draw the obejcts
chicken.draw()
backside.draw()


# flip to view the image
win.flip()


# wait for keypress to abort
event.waitKeys()

# close the window after keypress
win.close()