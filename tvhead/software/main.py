import pygame

pygame.init()
screen = pygame.display.set_mode((1400,1050))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    # load into screen
    pygame.display.flip()
    clock.tick(60) # 60 FPS

pygame.quit()
