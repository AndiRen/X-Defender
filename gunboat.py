import pygame
from invader import Invader
from pygame.constants import RLEACCEL
import my_colors

class Gunboat(Invader):
    
    def __init__(self, x, y, dx, dy, type):
       Invader.__init__(self, x, y, dx, dy, type)
       #self.type = 'gunboat'
       self.img = pygame.image.load('media/fighter1.png').convert()
       self.rate = 100
       self.shotSpeed = ''
       #self.img.set_colorkey((my_colors.white), RLEACCEL)
       #self.mark = count
       #self.img.set_colorkey((my_colors.white), RLEACCEL)
    
    ######################################################
    def fire(self):
        #if self.mark > 10000:
            #self.rate = 75
        
        #if self.shot == False and rate % 100 == 0 and self.y < 550: 
        #if self.mark % int(self.rate / (abs(self.dx) * 2)) == 0:
        if (self.x < 400 and self.dx < 0) or (self.x >= 400 and self.dx > 0):
            self.rate = 75
            if self.shot == False and self.y < 550 and self.mark % self.rate == 0:
                self.shotSpeed = 'double'
                self.shot = True    
        if (self.x >= 400 and self.dx < 0) or (self.x < 400 and self.dx > 0):
            self.rate = 100
            if self.shot == False and self.y < 550 and self.mark % self.rate == 0:
                self.shotSpeed = 'single'
                self.shot = True
        self.mark += 1
    ######################################################

    
        #if self.type == 'gunboat' and rate_calc == 0: #1000 == 0:
        #if self.type == 'gunboat':# and self.dx != 0 and self.mark % int(1000 / (abs(self.dx) * 20)) == 0: #
            #if self.mark > 100000:
                #rate = 250
            #else:
                #rate = 1000

                       
    
    
    
    
    #def fireIShots(self):
        #if self.dx != 0:
            #rate_calc = count % int(1000 / (abs(self.dx) * 20))
        #for s in iShots:
            #if s.fired == False and self.destroyed == False:
                #if self.type == 'fighter' and count % 3500 == 0:        
                    #s.fire(self)
                    #s.dx = 0
                    #s.dy = 0.12
                    #break      