import pygame
import random
import numpy as np

pygame.init()
screen = pygame.display.set_mode((1400,1050))
clock = pygame.time.Clock()
running = True

screen_move = 0
screen_speed = 0.25
width, height = 1400, 1050
# screen for chromatic abberation
surfaceca = pygame.Surface((screen.get_width(), screen.get_height()))
offsetca = random.sample(range(-3,3),6)

# Colors!
yellow = (255, 206, 7)
light_blue = (2, 168, 190)
dark_blue = (0, 114, 171)
white = (224, 238, 246)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surfaceca.fill(light_blue)
    for i in range(-2,6,2):
        pygame.draw.rect(surfaceca, dark_blue, pygame.Rect(0, screen_move+i*height/5, width, height/5))

        pygame.draw.rect(surfaceca, white, pygame.Rect(50, 50, 50, 50))
    # chromatic abberation
    arrayca = pygame.surfarray.array3d(surfaceca) #split into RGB
    for i in range(0,6):
        arrayca[:,:,i%3] = np.roll(arrayca[:,:,i%3], offsetca[i], axis=1-i//3)
    arrayca[:,:,:] += random.randint(0,3) # screen flicker
    pygame.surfarray.blit_array(surfaceca, arrayca)
    # load into screen
    screen.blit(surfaceca, (0,0))
    pygame.display.flip()
    clock.tick(60) # 60 FPS

    # update tick variables
    screen_move = screen_move+screen_speed if screen_move<height/2.5 else 0

pygame.quit()
