import pygame
import os
import random
# eyes
eye_idle = pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "idle.png")),0.5)
eye_blink = [
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "blink1.png")),0.5),
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "blink2.png")),0.5),
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "blink3.png")),0.5),
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "blink4.png")),0.5),
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "blink5.png")),0.5)
]
eye_doubleblink = [
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "doubleblink1.png")),0.5),
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "doubleblink2.png")),0.5),
    pygame.transform.scale_by(pygame.image.load(os.path.join("images", "eyes", "doubleblink3.png")),0.5)
]
# mouth
mouth_idle = pygame.transform.scale_by(pygame.image.load(os.path.join("images", "mouth", "idle.png")),0.5)

eye_current = eye_idle
mouth_current = mouth_idle
blink_timer = 0
blink_frame = 0
blinking = False

def update_face(surface, dt):
    global blinking, blink_timer, eye_current, blink_frame
    if blinking:
        blink_timer += dt
        if blink_frame == len(eye_blink):
            blink_frame = 0
            blinking = False
            eye_current = eye_idle
        elif blink_timer >= 1000/10:
            print("Frame elapse")
            eye_current = eye_blink[blink_frame]
            blink_frame = (blink_frame+1)
            blink_timer = 0

    surface.blit(eye_current, (0,0))
    surface.blit(mouth_current, (0,0))
    
def blink():
    global blinking
    blinking = True
    print("Blink")
   
