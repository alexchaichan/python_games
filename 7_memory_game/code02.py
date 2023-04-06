# import libraries
from psychopy import core, event, visual

# create the window
win = visual.Window(size=(960, 800), units='pix')

# create the chicken
chicken = visual.ImageStim(win, image="images/chicken/r01.png", size=(240, 400), units='pix')

# draw the chicken
chicken.draw()

# flip to view the image
win.flip()


# wait for keypress to abort
event.waitKeys()

# close the window after keypress
win.close()