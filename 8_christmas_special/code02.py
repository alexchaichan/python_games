# import some libraries
import os
from psychopy import core, event, visual

# create variables
## constants
BALL_SIZE = [0.025, 0.03, 0.04]
BALL_COLOR = ['red','blue','yellow']
BALL_POS = [(-0.125, -0.125), (0.125, 0.125), (0, 0)]


# drawing the window
win = visual.Window(size=(960, 800), units='norm')



# create the tree with a path
tree = visual.ImageStim(win, image=os.path.join("images", "pine-tree.png"), size=(0.5, 1), units='norm',)

# draw the tree (draw tree first!)
tree.draw()

# ballmachine (create some xmasballs)


for a_size, a_color, a_pos in zip(BALL_SIZE, BALL_COLOR, BALL_POS):

    balls = visual.Circle(win, radius=a_size, lineColor = "black", fillColor= a_color, pos=a_pos)
    
    # draw the balls (insde the for function!)
    balls.draw()


# flip the window
win.flip()

#waiting for key press to close the window
event.waitKeys()


#close the window 
win.close()