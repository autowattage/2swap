import gpiozero
import pygame
import os

# Until I can get my hands on an analog->digital convertor, this is the best I can do
mic_pin = 1
mic = gpiozero.DigitalInputDevice(mic_pin)

mouths = [
    pygame.image.load(os.path.join("images", "mouth", "idle.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk1.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk2.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk3.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk4.png"))
]

curr_mouth = None

def update_face(surface):
    global curr_mouth
    if mic.value > 0:
    	curr_mouth = mouths[3]
    else:
    	curr_mouth = mouths[0]
    
    surface.blit(curr_mouth, (0,-500))
   
