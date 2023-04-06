##unfortunatenly I couldn't manage to write the exact code you asked for, but I found a similar solution. 


# import some libraries
import os
from psychopy import core, event, visual, sound
#from psychopy.sound import Sound
import random
import yaml
with open("settings.yaml") as yaml_stream:
    settings = yaml.load(yaml_stream)

## variables to create xmasballs
BALL_SIZE = settings["balls"]["size"]
BALL_COLOR = settings["balls"]["color"]
BALL_POS = settings["balls"]["position"]

# create variables
# game state game run while 'running'
game_state = 'running'
#implement esc key
esc=['escape']



## variables to create twinkle
TWINKLE_DURATION = (0.5) # duration
i_color = [] # list of colors
color = ['red','blue','yellow'] # index variable that hold the color

song = sound.Sound(os.path.join("sounds", "Deck the Halls B.ogg"))

# drawing the window
win = visual.Window(size=(960, 800), units='norm')



song.play()

# starting the game loop / quit with esc
while game_state == 'running':


    # create the tree with a path
    tree = visual.ImageStim(win, image=os.path.join("images", "pine-tree.png"), size=(0.5, 1), units='norm',)
    # draw the tree (draw tree first!)
    tree.draw()


    # ballmachine (create some x-masballs)
    for a_size, a_color, a_pos in zip(BALL_SIZE, BALL_COLOR, BALL_POS):
        
        
        BALL_COLOR = random.sample(['red','blue','yellow'],3)

        balls = visual.Circle(win, radius=a_size, lineColor = "black", fillColor= a_color, pos=a_pos)

        
        # draw the balls (insde the for function!)
        balls.draw()
                
        core.wait(0.35)


    # flip the window
    win.flip()

    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == esc[0]:
            game_state = 'off'
