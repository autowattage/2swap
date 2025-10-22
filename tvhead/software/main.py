import pygame
import random
import numpy as np
import eyes, mouth, tilt

pygame.init()
flags = pygame.FULLSCREEN
screen = pygame.display.set_mode((1400, 1050), flags)
clock = pygame.time.Clock()
running = True

width, height = screen.get_width(), screen.get_height()
stripe_move = 0 #internal counter variable for screen
offsetca = random.sample(range(-3,3),6) #offset range for chromatic aberration

face_event = pygame.USEREVENT+1
pygame.time.set_timer(face_event, 1000)

# Colors!
yellow = (255, 206, 7)
light_blue = (2, 168, 190)
dark_blue = (2, 135, 172)
white = (224, 238, 246)

# draw background stripes
def draw_bgstripes(bgcolor, stripecolor):
    screen.fill(bgcolor)
    for i in range(-2,6,2):
        pygame.draw.rect(screen, stripecolor, pygame.Rect(0, stripe_move+i*height/5, width, height/5))

# apply chromatic abberation
def apply_ca(offset, flicker_offset):
    arrayca = pygame.surfarray.array3d(screen) #split into RGB
    for i in range(0,6):
        arrayca[:,:,i%3] = np.roll(arrayca[:,:,i%3], offset[i], axis=1-i//3)
    arrayca[:,:,:] += random.randint(0,flicker_offset) # screen flicker
    pygame.surfarray.blit_array(screen, arrayca)

while running:
    dt = clock.tick(500) # many fps..
    print(clock.get_fps())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif (not tilt.expression()) and (event.type == face_event):
            eyes.blink()
            pygame.time.set_timer(face_event, random.randint(1500,4000)) # 2500 6000
    draw_bgstripes(light_blue, dark_blue) #that cool striped background
    
    tilt.update_face(screen)
    if tilt.expression()==None:
    	mouth.update_face(screen)
    	eyes.update_face(screen, dt)

    # load into screen
    #apply_ca(offsetca, 5) #chromatic aberration -- use for lower fps
    pygame.display.flip()

    # update tick variables
    stripe_move = stripe_move+0.02*dt if stripe_move<height/2.5 else 0
    

pygame.quit()

