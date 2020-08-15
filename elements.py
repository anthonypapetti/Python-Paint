import pygame
import pickle
import tkinter
from tkinter import filedialog
from tkinter import *

class Cell():
    def __init__(self, posx, posy):
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.color = (255, 255, 255)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    #draws onto screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)
    
    #checks for clicks
    def Click(self, mouse):
        if mouse[0] > self.rect.topleft[0] and mouse[0] < self.rect.topright[0]:
            if mouse[1] > self.rect.topleft[1] and mouse[1] < self.rect.bottomleft[1]:
                return True

class Brush():
    def __init__(self):
        self.color = (0, 0, 0)
        self.size = 1
        self.position = None

class ColorPallate():
    def __init__(self, posx, posy, color):
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    #draws onto screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

    #checks for clicks    
    def Click(self, mouse):
        if mouse[0] > self.rect.topleft[0] and mouse[0] < self.rect.topright[0]:
            if mouse[1] > self.rect.topleft[1] and mouse[1] < self.rect.bottomleft[1]:
                return True
    
    def OnClick(self, brush):
        brush.color = self.color

class Border():
    def __init__(self, posx, posy):
        self.image = pygame.Surface((1000, 5))
        self.image.fill((201,201,201))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    #draws onto screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

class Button():
    def __init__(self, text, font, posx, posy, onclick):
        self.image = font.render(text, True, (0, 0, 0), (201,201,201))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.onclick = onclick
    
    #draws buttons onto the screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

    #checks for clicks    
    def Click(self, mouse):
        if mouse[0] > self.rect.topleft[0] and mouse[0] < self.rect.topright[0]:
            if mouse[1] > self.rect.topleft[1] and mouse[1] < self.rect.bottomleft[1]:
                return True

#takes a postion and raidus and returns a list of points
#within that square
def Draw_Circle(position: list, radius: int) -> list:
    k = radius * 2
    refpos = [position[0] - int(k / 2), position[1] - int(k / 2)]
    output = []
    for i in range(k + 1):
        for j in range(k + 1):
            output.append([refpos[0] + i, refpos[1] + j])
    return output

def resize(brush, size):
    brush.size = size

def clear_grid(grid):
    for row in grid:
        for cell in row:
            cell.image.fill((255, 255, 255))
            cell.color = (255, 255, 255)

def check_grid(grid):
    if not len(grid) == 110:
        return None
    for row in grid:
        if not len(row) == 200:
            return None
    for row in grid:
        for cell in row:
            if not isinstance(cell, Cell):
                return None
    return True

def save_grid(grid, root):
    root.withdraw()
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save File", filetypes=[("Pickle File", ".pickle")], defaultextension=[("Pickle File", ".pickle")])
    colorgrid = []
    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            row.append(grid[i][j].color)
        colorgrid.append(row)
    try:
        save_file = open(filename, "wb")
    except:
        return None
    
    pickle.dump(colorgrid, save_file)
    save_file.close()

def load_grid(grid, root):
    root.withdraw()
    filename = filedialog.askopenfilename(initialdir="/", title="Save File", filetypes=[("Pickle File", ".pickle")])
    infile = open(filename, "rb")
    new_grid = pickle.load(infile)
    # if not check_grid(new_grid):
    #     print("REEEEE")
    #     return None
    return new_grid