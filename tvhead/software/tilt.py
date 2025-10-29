import adafruit_bno055
import gpiozero
import board
import pygame
import os

i2c = board.I2C()
sensor = adafruit_bno055.BNO055_I2C(i2c)

expressions = [
    pygame.image.load(os.path.join("images", "expressions", "nervous.png")),
    pygame.image.load(os.path.join("images", "expressions", "excited.png")),
    pygame.image.load(os.path.join("images", "expressions", "surprised.png"))
]

curr_expr = None

def update_face(surface):
    global curr_expr, sensor
    rotation = sensor.euler
    print(rotation)
    #keys = pygame.key.get_pressed()
    if rotation[2] > 60:
    	curr_expr = expressions[0]
    elif rotation[0] < 60:
    	curr_expr = expressions[1]
    elif rotation[1] > 260:
    	curr_expr = expressions[2]
    else:
    	curr_expr = None
    if curr_expr:
    	surface.blit(curr_expr, (0,0))
    
def expression():
    global curr_expr
    return curr_expr
   
