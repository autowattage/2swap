import gpiozero
from gpiozero import Button
import time

#buttons = [Button(27), Button(22), Button(23), Button(17)]
active_buttons = [False, False, False, False]

def update_face():
    yay = Button(17)
    if yay.is_pressed:
        print("Pressed")
    else:
        print("Not pressed")
#def update_face():
#    global active_buttons, buttons
#    for index, button in enumerate(buttons):
#        if button.is_pressed:
#            active_buttons[index] = not active_buttons[index]
#        if active_buttons[index]:
#            print("Enabled button ", index)
#        else:
#            print("Disabled button ", index)

def active():
    return any(active_buttons)
