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
timer = 0
frame = 0
blinking = False
doubleblink = False
fps = 12
def update_face(surface, dt):
    global blinking, doubleblink, timer, eye_current, frame, fps
    timer += dt
    if blinking:
        if frame == len(eye_blink):
            eye_current = eye_idle
            frame = 0
            blinking = False
            doubleblink = random.random() > 0.5
        elif timer >= 1000/fps:
            eye_current = eye_blink[frame]
            frame += 1
            timer = 0
    if doubleblink:
        if frame == len(eye_doubleblink):
            eye_current = eye_idle
            frame = 0
            doubleblink = False
        elif timer >= 1000/fps:
            eye_current = eye_doubleblink[frame]
            frame += 1
            timer = 0

    surface.blit(eye_current, (0,0))
    surface.blit(mouth_current, (0,0))
    
def blink():
    global blinking
    blinking = True
   
