# import some libraries
from psychopy import core, event, visual
import os



# drawing the window
win = visual.Window(size=(960, 800), units='norm')

# create the tree with a path
tree = visual.ImageStim(win, image=os.path.join("images", "pine-tree.png"), size=(0.5, 1), units='norm')

# draw the tree
tree.draw()

# flip the window
win.flip()

#waiting for key press
event.waitKeys()


#close the window 
win.close()