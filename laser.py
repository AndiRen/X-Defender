import pygame
import my_colors

class Laser: 

    def __init__(self, ship, num):
        self.fired = True
        self.strike = False
        self.x = ship.x
        self.y = ship.y
        self.dx = 0
        self.dy = 0
        self.w = 0
        self.h = 0
        self.color = ''
        self.sType = ship.type
        self.hitType = ''
        self.destroyed = False
        self.volley = num
        self.fire(ship)
    
    def checkStrike(self, players, invaders, bosses):
        if self.sType != 'player':
            for p in players:
                if (self.x >= (p.x + 4) and self.x <= (p.x + 32)) and (self.y >= (p.y + 4) and self.y <= (p.y + 36)):
                    self.strike = True
                    p.destroy()
                    self.hitType = 'player'
        if self.sType == 'player':
            for i in invaders:
                    if (self.x >= (i.x + 5) and self.x <= (i.x + 35)) and (self.y >= (i.y + 5) and self.y <= (i.y + 27)):
                        self.strike = True
                        i.destroy()
                        self.hitType = 'invader'
        ###################################################
            for b in bosses:
                if (self.x >= b.x + 45 and self.x <= b.x + 200) and (self.y >= b.y + 30 and self.y <= (b.y + 50)):
                    self.strike = True
                    b.stg -= 1
                    self.hitType = 'boss'
                    shieldHit = pygame.mixer.Sound('media/laser_impact1.wav')
                    shieldHit.set_volume(0.25)
                    shieldHit.play()
                    if b.stg < 1:
                        b.destroy()
                        self.hitType ='bossDead'
                        laserHit = pygame.mixer.Sound('media/ship_explosion2.wav')
                        laserHit.set_volume(0.35)
                        laserHit.play()
            
        ###################################################
        if self.strike == True and self.hitType != 'boss':
            laserHit = pygame.mixer.Sound('media/ship_explosion.wav')
            laserHit.set_volume(0.25)
            laserHit.play()
            players[0].kills += 1
            self.dx = 0
            self.dy = 0
    
    def draw(self, screen):
        if self.sType == 'player':
            self.color = my_colors.laserGreen
        else:
            self.color = my_colors.laserRed

        if self.fired == True and self.strike == False:
            bullet = pygame.rect = (self.x, self.y, self.w, self.h)
            pygame.draw.rect(screen, self.color, bullet)
        if self.fired == False or self.strike == True:
            bullet = pygame.rect = (self.x, self.y, 0, 0)
            pygame.draw.rect(screen, my_colors.black, bullet)
            self.x = -100
            self.y = -100
            self.strike = False
    
    def move(self):
        if self.fired == True:
            self.y += self.dy
            self.x += self.dx
            if self.y > 525 or (self.x < 0 or self.x > 800):
                self.fired = False
                self.strike = False
                self.destroy()
    
    def fire(self, ship):
        if self.sType == 'player':
            self.x += 23
            self.y = self.y
            self.dx = 0
            self.dy = -2.5
            self.w = 3
            self.h = 12
        if self.sType == 'fighter':
            self.x += 16.5
            self.y += 35
            self.dx = 0
            self.dy = 1.75
            self.w = 3
            self.h = 12
        if self.sType == 'lander':
            self.x += + 16.5
            self.y += 35
            if self.x < 400:
                self.dx = 0.4
            if self.x > 400:
                self.dx = -0.4
            self.dy = 1.75
            self.w = 3
            self.h = 12
        if self.sType == 'gunboat': #"""""""""""""""""""""""""""""""""""""""""""
            self.x += 12
            self.y += 38
            self.w = 12
            self.h = 3
            self.dy = 0.4 + ship.dy

            if ship.shotSpeed == 'double':
                if ship.x < 400 and ship.dx < 0: #####
                    self.dx = 1.75 + abs(ship.dx)
                if ship.x >= 400 and ship.dx > 0:
                    self.dx = -1.75 - abs(ship.dx) #####
                
            if ship.shotSpeed == 'single':   
                if ship.x >= 400 and ship.dx < 0:
                    self.dx = -1.75 - abs(ship.dx)
                if ship.x < 400 and ship.dx > 0:
                    self.dx = 1.75 + abs(ship.dx)
            
            
            #print(ship.shotSpeed)
            #print('ship:', ship.dx, 'lazer:', self.dx)

        if self.sType == 'boss':
            if self.volley == 0:
                self.x += 200
                self.y += 65
                self.dx = 0
                self.dy = 1.75
                self.w = 3
                self.h = 12
            if self.volley == 1:
                self.x += 150
                self.y += 55
                self.dx = 0
                self.dy = 1.75
                self.w = 3
                self.h = 12
            if self.volley == 2:
                self.x += 100
                self.y += 45
                self.dx = 0
                self.dy = 1.75
                self.w = 3
                self.h = 12
            if self.volley == 3:
                self.x += 50
                self.y += 35
                self.dx = 0
                self.dy = 1.75
                self.w = 3
                self.h = 12
            
        laserSound = pygame.mixer.Sound('media/laser3.wav')
        laserSound.set_volume(0.15)
        laserSound.play()
    
    def destroy(self):
        self.destroyed = True