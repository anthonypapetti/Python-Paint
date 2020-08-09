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