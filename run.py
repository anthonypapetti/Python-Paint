import pygame
from pygame.locals import *
import sys
from elements import *

pygame.init()
pygame.display.set_caption("Python-Paint")

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
pallates = [
    ColorPallate(400, 600, colors["black"]),
    ColorPallate(450, 600, colors["red"]),
    ColorPallate(500, 600, colors["blue"]),
    ColorPallate(550, 600, colors["green"]),
    ColorPallate(400, 650, colors["pink"]),
    ColorPallate(450, 650, colors["purple"]),
    ColorPallate(500, 650, colors["teal"]),
    ColorPallate(550, 650, colors["yellow"])
]

#initalize fonts/UI text
UIfont = pygame.font.SysFont("arial", 30)
SizeText = UIfont.render("Brush Size:", False, (0, 0, 0))
ColorText = UIfont.render("Colors:", False, (0, 0, 0))
SaveText = UIfont.render("Save/load:", False, (0, 0, 0))

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
    for pallate in pallates:
        pallate.Draw(screen)
    
    #draw text
    screen.blit(SizeText, (100, 560))
    screen.blit(ColorText, (450, 560))
    screen.blit(SaveText, (750, 560))

    #draw cell grid
    for row in grid:
        for cell in row:
            cell.Draw(screen)
    
    #update display
    pygame.display.update()

pygame.quit()
sys.exit()