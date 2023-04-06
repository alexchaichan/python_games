# import libraries
from psychopy import visual, event
import random

# create some varialbe 
game_over = False 
keyList=['escape', 'space']

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

# text1 for quti
press_escape_text = visual.TextStim(win, "Press escape to exit", color=(0,1,0), bold = True, ) #exit text

# square
white_square = visual.Rect(win, pos=(150,-150), width=150, height=150, lineColor='purple', fillColor='pink')


while game_over == False:
    
    # drawing stimuli
    press_escape_text.draw()
    white_square.draw()
    
    
    # define random positions for the square
    x = random.uniform(-300,300)
    y = random.uniform(-300,300)
    
    
    # lets flip it
    win.flip()
    
    
    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == keyList[0]:
            game_over = True
        elif keys[0] == keyList[1]: #the entry in my list keys will always be overwritten, so I can always use the first entry in keys, even if I press space 5x and then esc
            white_square.pos = (x, y)