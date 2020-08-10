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
screen = pygame.display.set_mode(size)
screen.fill(colors["white"])

#init UI elements
border = Border(0, 550)
size1button = Button("1", UIfont, 120, 620, resize)
size2button = Button("2", UIfont, 160, 620, resize)
size3button = Button("3", UIfont, 200, 620, resize)

#init cell grid & Brush
brush = Brush()
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
    brush.position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #left click actions
        if pygame.mouse.get_pressed()[0]:
            #click on canvas
            if brush.position[1] < 550:
                #selecting target cell
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j].Click(brush.position):
                            #painting
                            circle = Draw_Circle([i, j], brush.size)
                            for position in circle:
                                try:
                                    grid[position[0]][position[1]].image.fill(brush.color)
                                    grid[position[0]][position[1]].color = brush.color
                                except:
                                    pass        
            #click on UI elements
            else:
                if size1button.Click(brush.position):
                    size1button.onclick(brush, 1)
                if size2button.Click(brush.position):
                    size2button.onclick(brush, 2)
                if size3button.Click(brush.position):
                    size3button.onclick(brush, 4)
        #right click actions
        if pygame.mouse.get_pressed()[2]:
            if brush.position[1] < 550:
                #selecting target cell
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if grid[i][j].Click(brush.position):
                            #painting
                            circle = Draw_Circle([i, j], brush.size)
                            for position in circle:
                                try:
                                    grid[position[0]][position[1]].image.fill((255,255,255))
                                    grid[position[0]][position[1]].color = (255,255,255)
                                except:
                                    pass
    
    #draw UI elements
    border.Draw(screen)
    for pallate in pallates:
        pallate.Draw(screen)
    size1button.Draw(screen)
    size2button.Draw(screen)
    size3button.Draw(screen)
    
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