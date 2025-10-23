import sounddevice as sd
from collections import deque
import threading
import numpy
import pygame
import os

mouths = [
    pygame.image.load(os.path.join("images", "mouth", "idle.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk1.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk2.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk3.png")),
    pygame.image.load(os.path.join("images", "mouth", "talk4.png"))
]

screen = None
curr_mouth = None
moving_avg = deque(maxlen=8)

def update_face(screen):
    global curr_mouth
    screen.blit(curr_mouth, (0,-500))
    
def get_volume(indata, outdata, frames, time, status):
    global curr_mouth, screen
    volume = int(numpy.linalg.norm(indata)*10)
    moving_avg.append(volume)
    volume = int(sum(moving_avg)*10 / len(moving_avg))
    print(volume)
    if volume>60:
    	curr_mouth = mouths[4]
    elif volume>40:
    	curr_mouth = mouths[3]
    elif volume>25:
    	curr_mouth = mouths[2]
    elif volume>11:
    	curr_mouth = mouths[1]
    else:
    	curr_mouth = mouths[0]

def start_audio_stream():  	
    with sd.Stream(channels=2, callback=get_volume):
        sd.sleep(100000)
        
audio_thread = threading.Thread(target=start_audio_stream)
audio_thread.start()

