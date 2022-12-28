import pygame
from pygame.constants import RLEACCEL
import my_colors

class Invader:
    
    def __init__(self, x, y, dx, dy, type):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        #self.type = 'invader'
        self.destroyed = False
        self.shot = False
        self.type = type
        self.mark = 0 #####
        self.img = pygame.image.load('media/fighter1.png').convert()
    
    def draw(self, screen):
        if self.destroyed == False:
            self.img.set_colorkey((my_colors.white), RLEACCEL)
            screen.blit(self.img, (self.x, self.y))
            #marker = pygame.rect =(self.x, self.y, 2, 2)
            #pygame.draw.rect(screen, my_colors.red, marker)
    
    def move(self):
        self.land()
        self.changeDirection()
        self.x += self.dx
        self.y += self.dy
    
    def land(self):
        if self.y > 550:
            self.dy = 0
            if self.x <= 386 and self.x >= 384 and self.y < 580:
                self.dx = 0
                self.dy = 0.25
                self.x = 385
            elif self.x > 386:
                self.dx = -0.5
            elif self.x <= 384:
                self.dx = 0.5
    
    def changeDirection(self):
        if self.x > 750 or self.x < 50:
            if self.dy == 0 and self.y < 550:
                self.y += 1.75
            if self.x > 760 or self.x < 40:
                self.dx *= -1
            
    def __del__(self):
        pass
        #print('Invader destroyed!')

    def destroy(self):
        self.x = -500
        self.y = -500
        self.dx = 0
        self.dy = 0
        self.destroyed = True
    
    #####
    def update(self):
        self.shot = False