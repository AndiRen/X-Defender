#Player class file

import pygame
from pygame.constants import RLEACCEL
import my_colors

class Player:

    def __init__(self, x, y, dx, dy, type):
        self.x = x
        self.y = y
        self.dx = dx #cant i just put these to 0??
        self.dy = dy #cant i just put these to 0??
        self.type = type
        self.kills = 0
        self.ammo = 10
        self.destroyed = False
        self.left_key = False
        self.right_key = False
        self.up_key = False
        self.down_key = False
        self.space = False
        self.shot = False
        self.img = pygame.image.load('media/myShip2.png').convert()
    
    def draw(self, screen):
        if self.destroyed == False:
            self.img.set_colorkey((my_colors.white), RLEACCEL)
            screen.blit(self.img,  (self.x, self.y))       
    
    def move(self):
        
        #Precise Movement
        #self.dx = 0
        #self.dy = 0
        
        if self.destroyed == False:
            if self.left_key == True and self.dx > -2.5:
                self.dx -= 0.25
            if self.right_key == True and self.dx < 2.5:
                self.dx += 0.25
            if self.up_key == True and self.dy > -1.5:
                self.dy -= 0.15
            if self.down_key == True and self.dy < 1.5:
                self.dy += 0.15
            
            #Fluid Movement
            ######################################################
            if self.left_key == False and self.right_key == False:
                if self.dx > 0:
                    self.dx -= 0.1
                if self.dx < 0:
                    self.dx += 0.1
                if self. dx < 0.1 and self.dx > - 0.1:
                    self.dx = 0

            if self.up_key == False and self.down_key == False:
                if self.dy > 0:
                    self.dy -= 0.05
                if self.dy < 0:
                    self.dy += 0.05
                if self. dy < 0.1 and self.dy > - 0.1:
                    self.dy = 0
            ######################################################

        if self.x < 10 or self.x > 740:
            self.dx = 0
            if self.x < 10:
                self.x = 11
            if self.x > 740:
                self.x = 739
        
        if self.y < 50 or self.y > 500:
            self.dy = 0
            if self.y < 50:
                self.y = 51
            if self.y > 500:
                self.y = 499
        
        self.x += self.dx
        self.y += self.dy
    
    def fire(self):
        if self.space == True:
            if self.ammo > 0:
                self.shot = True
                self.ammo -= 1
        self.space = False
    
    def updateInfo(self, count):
        if count % 50 == 0 and self.ammo < 10:
            self.ammo += 1
    
    def destroy(self):
        self.x = -500
        self.y = -500
        self.dx = 0
        self.dy = 0
        self.destroyed = True
