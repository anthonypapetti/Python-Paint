import pygame
from pygame.locals import *
import sys
from elements import *

pygame.init()

#colors
colors = {
    "white": (255, 255, 255),
    "black": (0,0,0),
    "red": (255, 0, 0),
    "blue": (0, 255, 0),
    "green": (0, 0, 255),
    "pink": (255, 153, 238),
    "purple": (187, 51, 255),
    "teal": (128, 255, 255),
    "yellow": (255, 255, 0)
    }

#initalize screen
size = (1000, 700)
cellsize = (int(size[0]/5), int(550/5))
print(cellsize)
screen = pygame.display.set_mode(size)
screen.fill(colors["white"])

#init UI elements
border = Border(0, 550)

#init cell grid
grid = []

xptr = 0
yptr = 0
for i in range(cellsize[1]):
    row = []
    for j in range(cellsize[0]):
        row.append(Cell(xptr, yptr))
        xptr += 5
    yptr += 5
    xptr = 0
    grid.append(row)


run = True
while run:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #left click actions
        if pygame.mouse.get_pressed()[0]:
            #click on canvas
            if mouse[1] < 550:
                for row in grid:
                    for cell in row:
                        if cell.Click(mouse):
                            cell.image.fill((0,0,0))
            #click on UI elements
            else:
                print("below border")
        #right click actions
        if pygame.mouse.get_pressed()[2]:
            if mouse[1] < 550:
                for row in grid:
                    for cell in row:
                        if cell.Click(mouse):
                            cell.image.fill((255,255,255))
    
    #draw UI elements
    border.Draw(screen)

    #draw cell grid
    for row in grid:
        for cell in row:
            cell.Draw(screen)
    
    #update display
    pygame.display.update()

pygame.quit()
sys.exit()