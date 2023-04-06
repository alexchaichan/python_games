# import libraries
from psychopy import visual, event
import random
import os


def position_from_index(i_chicken):
    
    if i_chicken <= 3:
        x = -0.75+0.5*i_chicken
        y = 0.5
    else:
        x = -0.75+(-0.5)*-i_chicken -2
        y = -0.5
    
    return x, y
    
    
    
def mouse_index(pos):
    
    mouse.getPos
    return x, y


# create some varialbe 
game_over = False 
keyList=['escape']

# creat index for chickens
i_chicken = range(0,8)
#extract the single files inside the directory
image=[x for x in os.listdir("images/chicken")*2 if x.startswith('l')]
#shuffle the pictures
image = random.sample(image, 8)

# creating a 800 x 600 window
win = visual.Window(size=(960, 800), units='norm')
mouse = event.Mouse(visible=True, win=win)


while game_over == False:
    


    
    
    for card in i_chicken:
        
        
        
        # create the path for each chicken picture
        path = os.path.join("images", "chicken", image[card]) 
        
        card = {
        'front' : visual.ImageStim(win, image=path, size=(0.5, 1), units='norm', pos=(position_from_index(card))),
        'back' : visual.Rect(win, units='norm',size=(0.5,1), pos=(position_from_index(card)), lineColor='white', fillColor='cyan'),
        'side' : None,
        'show' : True
        }
        # update the card
        card['side'] = card['back']
        
        
        buttons = mouse.getPressed()
        press_key_text = visual.TextStim(win, buttons, color=(0,1,0), bold = True) #exit text
        press_key_text.draw()
        
        pos = (round(mouse.getPos()[0],1), round(mouse.getPos()[1],1))
        press_key_pos = visual.TextStim(win, pos, pos=(-0.5, -0.5), color=(0,1,0), bold = True) #exit text
        press_key_pos.draw()
        
        card['side'].draw()
    
    win.flip()
        

        
        
    
    
    # lets flip it
   
    
    
    # end the game with esc
    keys = event.getKeys()
    if keys:
        # define the keylist
        if keys[0] == keyList[0]:
            game_over = True
