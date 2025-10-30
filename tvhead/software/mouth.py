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


curr_mouth = mouths[0]
moving_avg = deque(maxlen=8)

def update_face(screen):
    global curr_mouth, mouths
    #print(curr_mouth)
    screen.blit(curr_mouth, (0,0)) #-500 bc my screen too small lol
    
def get_volume(indata, frames, time, status):
    global mouths, curr_mouth, screen
    #print(sd.query_devices())
    volume = int(numpy.linalg.norm(indata)*10)
    moving_avg.append(volume)
    volume = int(sum(moving_avg)*5/ len(moving_avg))
    #print(volume*"|")
    if volume>30:
    	curr_mouth = mouths[4]
    elif volume>22:
    	curr_mouth = mouths[3]
    elif volume>10:
    	curr_mouth = mouths[2]
    elif volume>3:
    	curr_mouth = mouths[1]
    else:
    	curr_mouth = mouths[0]

def start_audio_stream():  	
    with sd.InputStream(channels=2, callback=get_volume):
        sd.sleep(1000000)

# thread for audio because it cant run same time as pygame...
audio_thread = threading.Thread(target=start_audio_stream)
audio_thread.start()

