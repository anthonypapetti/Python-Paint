import pygame
from pygame.locals import *
import sys

pygame.init()

#colors
colors = {
    "white": [255, 255, 255],
    "black": [0,0,0],
    "red": [255, 0, 0]
    "blue": [0, 255, 0],
    "green": [0, 0, 255],
    "pink": [255, 153, 238],
    "purple:" [187, 51, 255],
    "teal": [128, 255, 255]
    "yellow": [255, 255, 0]
    }

#screen size
size = (1000, 700)

screen = pygame.display.set_mode(size)

screen.fill(colors["white"])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
sys.exit()