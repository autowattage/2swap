import gpiozero

import pygame
import os

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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_v]:
    	curr_mouth = mouths[4]
    elif keys[pygame.K_c]:
    	curr_mouth = mouths[3]
    elif keys[pygame.K_x]:
    	curr_mouth = mouths[2]
    elif keys[pygame.K_z]:
    	curr_mouth = mouths[1]
    else:
    	curr_mouth = mouths[0]
    
    surface.blit(curr_mouth, (0,0))
   
