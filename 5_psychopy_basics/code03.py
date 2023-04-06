# import libraries
from psychopy import visual, event

# create some varialbe 
game_over = False 
keyList=['escape']

# creating a 800 x 600 window
win = visual.Window(size=(800, 600))

press_escape_text = visual.TextStim(win, "Press escape to exit", color=(0,1,0), bold = True, ) #exit text


while game_over == False:
    
    # drawing stimuli
    press_escape_text.draw()
    
    # lets flip it
    win.flip()
    
    
    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist7
        if keys[0] == keyList[0]:
            game_over = True


