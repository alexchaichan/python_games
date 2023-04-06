# import libraries
from psychopy import core, event, visual

#import utils
def position_from_index(index):
    
    if index <= 3:
        x = -0.75+0.5*index
        y = 0.5
    else:
        x = -0.75+(-0.5)*-index -2
        y = -0.5
    
    return x, y

# create a window
win = visual.Window(size=(960, 800), units='norm')

# creat index for chickens
i_chicken = [0, 1, 2, 3, 4, 5, 6, 7]

# create a card
card = {
'front' : visual.ImageStim(win, image="images/chicken/r01.png", size=(0.5, 1), units='norm', pos=(position_from_index(i_chicken[5]))),
'back' : visual.Rect(win, units='norm',size=(0.5,1), pos=(position_from_index(i_chicken[5])), lineColor='white', fillColor='black'),
'filename' : 'r01',
#'side' : visual.Rect(win, units='norm',size=(0.5,1), pos=(position_from_index(i_chicken[5])), lineColor='white', fillColor='black'),
'show' : True
}

card = {
'side' : card['back']
} #my attempt card['front', 'back', 'side']


# draw the obejcts
card['side'].draw()

# flip to view the image
win.flip()


# wait for keypress to abort
event.waitKeys()

# close the window after keypress
win.close()