import pygame
from invader import Invader
from laser import Laser
from pygame.constants import RLEACCEL
import my_colors

class Fighter(Invader):
    
    def __init__(self, x, y, dx, dy, type):
       Invader.__init__(self, x, y, dx, dy, type)
       #self.type = 'fighter'
       self.img = pygame.image.load('media/fighter1.png').convert()
       #self.img.set_colorkey((my_colors.white), RLEACCEL)
       #self.mark = count
       #self.img.set_colorkey((my_colors.white), RLEACCEL)
       
    def fire(self):
        if self.shot == False and self.mark % 200 == 0 and self.y < 550: #####
            self.shot = True
        self.mark += 1
        
        
        
        
        
        
        
        #if self.dx != 0:
            #rate_calc = count % int(1000 / (abs(self.dx) * 20))
        #for s in iShots:
            #if s.fired == False and self.destroyed == False:
                
                    #s.fire(self)
                    #s.dx = 0
                    #s.dy = 0.12
                    #break   