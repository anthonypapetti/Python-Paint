import pygame

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
        self.size = 2
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


#takes a postion and raidus and returns a list of points
#within that square
# ONLY USE RADIUS VALUES DIVISIBLE BY 2
def Draw_Circle(position: list, radius: int) -> list:
    k = radius * 2
    l = radius
    refpos = [position[0], position[1] + l]
    output = []
    while True:
        for i in range(l):
            output.append([refpos[0] + i, refpos[1]])
        for i in range(k):
            output.append([refpos[0] + l, refpos[1] - i])
        for i in range(k):
            output.append([refpos[0] + l - i, refpos[1] - k])
        for i in range(k):
            output.append([refpos[0] - l, refpos[1] - k + i])
        for i in range(l):
            output.append([refpos[0] - l + i, refpos[1]])
        refpos[1] -= 1
        if refpos == position:
            output.append(refpos)
            return output
        k = int(k / 2)
        l = int(l / 2)