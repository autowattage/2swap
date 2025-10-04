import pygame
import os
import random
# eyes
eye_idle = pygame.image.load(os.path.join("images", "eyes", "idle.png"))
eye_blink = [
    pygame.image.load(os.path.join("images", "eyes", "blink1.png")),
    pygame.image.load(os.path.join("images", "eyes", "blink2.png")),
    pygame.image.load(os.path.join("images", "eyes", "blink3.png")),
    pygame.image.load(os.path.join("images", "eyes", "blink4.png")),
    pygame.image.load(os.path.join("images", "eyes", "blink5.png"))
]
eye_doubleblink = [
    pygame.image.load(os.path.join("images", "eyes", "doubleblink1.png")),
    pygame.image.load(os.path.join("images", "eyes", "doubleblink2.png")),
    pygame.image.load(os.path.join("images", "eyes", "doubleblink3.png"))
]
# mouth
mouth_idle = pygame.image.load(os.path.join("images", "mouth", "idle.png"))

eye_current = eye_idle
mouth_current = mouth_idle
timer = 0
frame = 0
anim_playing = [False, False]
fps = 12

def animate(frames, anim_id):
    global eye_current, anim_playing, eye_idle, frame, timer
    if anim_playing[anim_id]:
        if frame == len(frames):
            eye_current = eye_idle
            frame = 0
            anim_playing[anim_id] = False
            if anim_id==0 and random.random()>0.5:
                anim_playing[1] = True
        elif timer >= 1000/fps:
            eye_current = frames[frame]
            frame += 1
            timer = 0
    
def update_face(surface, dt):
    global timer
    timer += dt

    animate(eye_blink, 0)
    animate(eye_doubleblink, 1)

    surface.blit(eye_current, (0,0))
    surface.blit(mouth_current, (0,0))
    
def blink():
    global anim_playing
    anim_playing[0] = True
   
