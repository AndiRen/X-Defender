import pygame
from pygame.constants import RLEACCEL
import my_colors


class Boss:

    def __init__(self, x, y, dx, dy, stg, type, count):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.stg = stg #####
        self.mark = count
        self.shot = False
        self.destroyed = False
        self.type = type
        self.img = pygame.image.load('media/boss3.png').convert()
    
    def draw(self, screen):
        if self.destroyed == False:
            self.img.set_colorkey((my_colors.white), RLEACCEL)
            screen.blit(self.img,  (self.x, self.y)) 
            
            #T1marker = pygame.rect =(self.x + 45, self.y, 2, 2)
            #pygame.draw.rect(screen, my_colors.red, T1marker)
            #T2marker = pygame.rect =(self.x + 200, self.y, 2, 2)
            #pygame.draw.rect(screen, my_colors.red, T2marker)

            #B1marker = pygame.rect =(self.x + 45, self.y + 30, 2, 2)
            #pygame.draw.rect(screen, my_colors.red, B1marker)
            #B2marker = pygame.rect =(self.x + 200, self.y + 50, 2, 2)
            #pygame.draw.rect(screen, my_colors.red, B2marker)
    
    def move(self):
        self.changeDirection()
        self.x += self.dx
        self.y += self.dy
    
    def changeDirection(self):
        if self.y > 40:
            self.dy = 0
            self.y = 40
            self.dx = -0.25
        if self.x < 225 or self.x > 425:
            self.dx *= -1

    def __del__(self):
        pass

    def destroy(self):
        self.x = -1000
        self.y = -1000
        self.dx = 0
        self.dy = 0
        self.destroyed = True

    def fire(self, count):
        if self.shot == False and count > 9500 and self.mark % 200 == 0 and self.y >= 40: 
            self.shot = True
        self.mark += 1