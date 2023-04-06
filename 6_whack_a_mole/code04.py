# import libraries
from psychopy import visual, event

#create variables
game_over = False
keyList=['escape']

# creating a 800 x 600 window
win = visual.Window(size=(800, 600), units='pix')

# creat some moles

i_moles = range(3)

# creat some moles
moles = [
visual.Circle(win, pos=(150,-150), radius=75, edges=32, units='pix', lineColor='purple', fillColor='pink'),
visual.Circle(win, pos=(-150,150), radius=75, edges=32, units='pix', lineColor='purple', fillColor='pink'),
visual.Circle(win, pos=(0,0), radius=75, edges=32, units='pix', lineColor='purple', fillColor='pink')
]


# start loop
while game_over == False:
    
    
    for x in i_moles:
        moles[x].draw()
        
    
    # lets flip it
    win.flip()
    
    
    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == keyList[0]:
            game_over = True