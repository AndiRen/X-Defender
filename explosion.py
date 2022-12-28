import pygame
from pygame.constants import RLEACCEL
import my_colors

class Explosion:
    
    def __init__(self, limit, expFile, x, y, type): #####type
        self.exp = False
        self.x = 0
        self.y = 0
        self.adjustX = x
        self.adjustY = y
        self.expCount = 0
        self.countLimit = limit
        self.expFile = expFile
        self.type = type

    def trigger(self, ship): #x, y, hType):
        if ship.hitType == self.type:
            self.exp = True
            self.x = ship.x
            self.y = ship.y

    def draw(self, screen):
        if self.exp == True and self.expCount < self.countLimit:
            explosion = pygame.image.load(self.expFile).convert()
            explosion.set_colorkey((my_colors.white), RLEACCEL)
            screen.blit(explosion, ((self.x + self.adjustX), (self.y + self.adjustY)))    
            if self.type == 'bossDead':
                explosion = pygame.image.load('media/explosion3.png').convert()
                explosion.set_colorkey((my_colors.white), RLEACCEL)
                screen.blit(explosion, (self.x -18, self.y -21))
                screen.blit(explosion, (self.x -12, self.y + 13))
                screen.blit(explosion, (self.x, self.y -3))
                
            self.expCount += 1
        
        if self.expCount == self.countLimit:
           self.exp = False 
           self.expCount = 0
            
            
            
            
            