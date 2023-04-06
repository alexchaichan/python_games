"""
A minimal PsychoPy code.
"""

# this imports two modules from psychopy
# visual has all the visual stimuli, including the Window class
# that we need to create a program window
# event has function for working with mouse and keyboard
from psychopy import visual, event

# creating a 800 x 600 window
win = visual.Window(size=(800, 600))

# waiting for any key press
event.waitKeys()

# closing the window
win.close()