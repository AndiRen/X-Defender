#Test Game Loop

import pygame
import random
from pygame.constants import RLEACCEL
from menu import *
from player import Player
from invader import Invader
from fighter import Fighter
from lander import Lander
from gunboat import Gunboat
from boss import Boss
from laser import Laser
from explosion import Explosion
import my_colors

class GameLoop:

    def __init__(self):

        #Setup ##########################################################
        pygame.init()
        
        #Display window info
        pygame.display.set_caption("Andy's X-Defender")
        icon = pygame.image.load('media/xDefender.png')
        pygame.display.set_icon(icon)
        pygame.mouse.set_visible(False)
        
        self.running = True
        self.playing = False

        #Screen
        self.DISPLAY_W = 800
        self.DISPLAY_H = 600
        self.screen = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.alpha = 175 #low less visible
        self.alpha2 = 50
        self.bkgSurface = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.alphaSurf1 = pygame.Surface((165, 63), flags=pygame.SRCALPHA)
        self.alphaSurf2 = pygame.Surface((180, 22), flags=pygame.SRCALPHA)
        self.alphaSurf3 = pygame.Surface((400, 240), flags=pygame.SRCALPHA)


        #########################################################################
        #self.alpha = 200
        #self.alphaSurface1 = pygame.Surface((140, 60), flags = pygame.SRCALPHA)
        #self.alphaSurface2 = pygame.Surface((140, 30), flags = pygame.SRCALPHA)
        #########################################################################

        #Game loop variables
        self.count = 0
        self.level = 'demo'
        self.waitCount = 0
        self.gameOver = False
        self.gameCondition = ''

        self.clock = pygame.time.Clock()
        self.clock.tick(100)

        #Background music
        self.bgMusic = pygame.mixer.Sound('media/BkgLoop3.mp3')
        self.bgMusic.set_volume(0.3)

        #################################################################

        #Objects ########################################################
        self.invaders = []
        self.lasers = []
        self.bosses = []
        self.players = []
        self.explosions = []
        self.buildings = []
        self.stars = []
        #self.menus = []

        self.createCity()

        self.player = Player(378, 499, 0, 0, 'player')
        self.boss = Boss(-1000, -1000, 0, 0, 30, 'boss', self.count)
        self.sExp = Explosion(200, 'media/explosion4.png', -30, -10, 'player')
        self.iExp = Explosion(100, 'media/explosion4.png', -22 , -25, 'invader')
        self.bExp = Explosion(300, 'media/explosion5.png', -80, -60, 'bossDead')

        self.players.append(self.player)
        self.explosions.append(self.sExp)
        self.explosions.append(self.iExp)
        self.explosions.append(self.bExp)
        self.bosses.append(self.boss)

        #Menu
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
        self.mainMenu = MainMenu(self)
        self.credits = CreditsMenu(self)
        self.options = OptionsMenu(self)
        self.curMenu = self.mainMenu

        #self.menus.append(self.mainMenu)
        #self.menus.append(self.credits)
        #self.menus.append(self.options)
    #################################################################

    #Functions ######################################################

    #Menu functions
    def clearKeys(self):
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False
    
    #Setup Function
    def createCity(self):
        numb = random.randint(25, 75)
        nums = random.randint(25, 125)
                
        for b in range(numb):
            x = random.randint(0, 800)
            w = random.randint(15, 25)
            h = random.randint(15, 65)
            bld = pygame.rec = (x, (590 - h), w, h, )
            self.buildings.append(bld)
                
        for s in range(nums):
            x = random.randint(0, 800)
            y = random.randint(0, 510)
            star = pygame.rec = (x, y, 2, 2)
            self.stars.append(star)
        ################################################
                    
    def drawCity(self):
        base = pygame.rect =(0, 590, 800, 15)
        pygame.draw.rect(self.bkgSurface, my_colors.darkGreen, base) #self.screen

        for b in self.buildings:
            pygame.draw.rect(self.bkgSurface, my_colors.darkGrey, b) #self.screen
                
        for s in self.stars:
            pygame.draw.rect(self.bkgSurface, my_colors.white, s) #self.screem
        ################################################

    #In-game functions #################################
    def printText(self, font, text, color, pos, x, y, scr): #bkg after color
        
        font = font
        text = font.render(text, True, color) # ,bkg
        textRect = text.get_rect()
        
        if pos == 'topleft':
            textRect.topleft = (x, y)
        if pos == 'topright':
            textRect.topright = (x, y)
        if pos == 'bottomleft':
            textRect.bottomleft = (x, y)
        if pos == 'bottomright':
            textRect.bottomright = (x, y)
        if pos == 'center':
            textRect.center = (x, y)

        #can use pos argument to blit to different alphaSurfaces
        if scr == 'bkg':
            self.bkgSurface.blit(text, textRect)
        if scr == 'a1':
            self.alphaSurf1.blit(text, textRect)
        if scr == 'a2':
            self.alphaSurf2.blit(text, textRect)
        if scr == 'a3':
            self.alphaSurf3.blit(text, textRect)
        ################################################
    
    def printInfo(self):        
        font = pygame.font.SysFont('OCR A Extended', 28)
        text3 = "Kills: " + str(self.player.kills)
        text4 = " Boss Strength: " + str(self.boss.stg)
        text5 = "Laser Charge: " + str(self.player.ammo)
        text6 = "Level: " + str(self.level)

        self.printText(font, text4, my_colors.white, 'topleft', 0, 0, 'a2') ##### topright
        self.printText(font, text6, my_colors.white, 'topleft', 0, 0, 'a1')
        self.printText(font, text5, my_colors.white, 'topleft', 0, 20, 'a1')
        self.printText(font, text3, my_colors.white, 'topleft', 0, 40, 'a1')

        self.displayEnd()

        ################################################

    #Action functions
    def moveAll(self):
        for p in self.players:
            p.move()
        
        for i in self.invaders:
            i.move()
        
        for b in self.bosses:
            b.move()
        
        for l in self.lasers:
            l.move()
        ################################################

    def drawAll(self):
        for e in self.explosions:
            e.draw(self.bkgSurface)

        for i in self.invaders:
            i.draw(self.bkgSurface)
        
        for b in self.bosses:
            b.draw(self.bkgSurface)
        
        for p in self.players:
            p.draw(self.bkgSurface)
        
        for l in self.lasers:
            l.draw(self.bkgSurface)
        ################################################

    def fireAll(self):

        for p in self.players:
            if p.destroyed == False and p.shot == True:
                laser = Laser(p, 1)
                self.lasers.append(laser)
                p.shot = False
        for i in self.invaders:
            if i.destroyed == False and i.shot == True:
                laser = Laser(i, 1)
                self.lasers.append(laser)
                i.shot = False
        for b in self.bosses:
                if b.destroyed == False and b.shot == True:
                    for n in range(4):
                        laser = Laser(b, n)
                        self.lasers.append(laser)
                    b.shot = False

        for p in self.players:
            p.fire()
        
        for i in self.invaders:
            i.fire()
        
        for b in self.bosses:
            b.fire(self.count)
        ################################################

    def updateAll(self):
        for p in self.players:
            p.updateInfo(self.count)

        for l in self.lasers:
            l.checkStrike(self.players, self.invaders, self.bosses)

        for l in self.lasers:
            if l.strike == True:
                for e in self.explosions:
                    e.trigger(l)
        ################################################

    def destroyObjects(self):
        for i in self.invaders:
            if i.destroyed == True:
                del i
        
        for l in self.lasers:
            if l.x < 0 or l.x > 800 or l.y < 0 or l.y > 600:
                del l
        
        for p in self.players:
            if p.destroyed == True:
                del p
        
        for b in self.bosses:
            if b.destroyed == True:
                del b
        ################################################

    def checkGameWin(self):
        
        if self.boss.destroyed == True:
            if self.waitCount > 305:
                self.gameOver = True
                self.gameCondition = 'win'
                print('win!')
        
        if self.player.destroyed == True:
            if self.waitCount > 205:    
                self.gameOver = True
                self.gameCondition = 'loose'
                print('loose!')

        for i in self.invaders:
            if i.x <= 386 and i.x >= 384 and i.y >= 580:
                self.gameOver = True
                self.gameCondition = 'loose'
                print('loose!')
                
        ################################################
    #Display end screen ################################
    def displayEnd(self):
        font = pygame.font.SysFont('OCR A Extended', 55)
        font2 = pygame.font.SysFont('OCR A Extended', 75)

        text1 = 'Win!'
        text2 = 'Loose!'
        text3 = 'ESC for Main Menu'
        text4 = 'Q to quit'

        if self.gameOver == True:
            if self.gameCondition == 'win':
                self.printText(font2, text1, my_colors.white, 'center', 400, 100, 'bkg')
            if self.gameCondition == 'loose':
                self.printText(font2, text2, my_colors.white, 'center', 400, 100, 'bkg')
            self.printText(font, text3, my_colors.white, 'center', 200, 80, 'a3') #400, 215, 'bkg'
            self.printText(font, text4, my_colors.white, 'center', 200, 160, 'a3') #400, 265, 'bkg'
        ################################################
    #Arrange invader approaches ########################
    def arrangeInvaders(self):
        
        if self.count < 3000:
            dx = 0.5
            dy = 0.25
        elif self.count < 4000:
            dx = 0.6
            dy = 0.25
        elif self.count < 5500:
            dx = 0.7
            dy = 0.3
        elif self.count < 7000:
            dx = 0.8
            dy = 0.35
        elif self.count < 8000:
            dx = 0.9
            dy = 0.4
        elif self.count < 9000:
            dx = 1
            dy = 0.45
        else:
            dx = 1.2
            dy = 0.5
        
        if (self.count % 1000 == 0) and self.count < 9000: #####
            invader1 = Fighter(40, -20, dx, 0, 'fighter')
            self.invaders.append(invader1)
        if  (self.count > 0 and self.count % 1500 == 0) and self.count < 9000:
            for n in range(2):
                if n == 0:
                    invader2 = Lander(720, -20, 0, dy, 'lander')
                else:
                    invader2 = Lander(50, -20, 0, dy, 'lander')
                self.invaders.append(invader2)
        if ((self.count > 0 and self.count % 2200 == 0) or (self.count > 0 and self.count % 2400 == 0)) and self.count < 9000:
            if self.count % 2400 == 0:
                invader3 = Gunboat(425, -20, dx, dy, 'gunboat') #####
            else:
                invader3 = Gunboat(375, -20, -dx, dy, 'gunboat') #####
            self.invaders.append(invader3)
        if (self.count > 1500 and self.count % 1300 == 0) and self.count < 9000:
            invader4 = Fighter(720, -20, dx, 0, 'fighter')
            self.invaders.append(invader4)
        if (self.count > 2500 and self.count % 1600 == 0) and self.count < 9000:
            for n in range(2):
                if n == 0:
                    invader5 = Lander(470, -20, 0, dy, 'lander')
                else:
                    invader5 = Lander(280, -20, 0, dy, 'lander')
                self.invaders.append(invader5)
        if self.count == 9500:
            self.boss.x = 375
            self.boss.y = -65
            self.boss.dy = 0.25
        if self.count > 10000 and self.count % 300 == 0:
            invader6 = Gunboat(self.boss.x + 140, self.boss.y + 35, 0.5, .25, 'gunboat')
            invader7 = Fighter(self.boss.x + 140, self.boss.y + 35, -.75, .35, 'fighter')
            self.invaders.append(invader6)
            self.invaders. append(invader7)
        ################################################

    #loop fucntions ####################################
    def processEvents(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                self.curMenu.runDisplay = False
            
            #Check for keystrokes
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_LEFT:
                    self.player.left_key = True
                if event.key == pygame.K_RIGHT:
                    self.player.right_key = True
                if event.key == pygame.K_UP:
                    self.player.up_key = True
                    if self.playing != True:#######################################
                            self.UP_KEY = True
                if event.key == pygame.K_DOWN:
                    self.player.down_key = True
                    if self.playing != True:#######################################
                            self.DOWN_KEY = True
                if event.key == pygame.K_SPACE:
                    self.player.space = True
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.BACK_KEY = True
                if event.key == pygame.K_q:
                    if self.gameOver == True:
                        pygame.quit()

            if event.type ==pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.left_key = False
                if event.key == pygame.K_RIGHT:
                    self.player.right_key = False
                if event.key == pygame.K_UP:
                    self.player.up_key = False
                if event.key == pygame.K_DOWN:
                    self.player.down_key = False

    #Take actions ###########################################
    def gameActions(self):
        
        if self.gameOver == False:
            self.moveAll() 
            self.fireAll() 
            self.updateAll()
            #self.destroyObjects()
            self.checkGameWin()
            self.arrangeInvaders()

            self.count += 1
            #print(self.count)

            if self.boss.destroyed == True or self.player.destroyed == True:
                self.waitCount += 1
                #print(waitCount)
        #####################################################

    #Display screen ###########################################
    def displayScreen(self):
        
        self.bkgSurface.fill(my_colors.black)
        self.alphaSurf1.fill(pygame.Color(0, 0, 0, self.alpha)) #must enter all 4 as tuple together
        self.alphaSurf2.fill(pygame.Color(0, 0, 0, self.alpha))
        self.alphaSurf3.fill(pygame.Color(255, 255, 255, self.alpha2))

        self.drawCity()
        self.drawAll()
        self.printInfo()

        self.screen.blit(self.bkgSurface, (0, 0))
        self.screen.blit(self.alphaSurf1, (0, 0))
        self.screen.blit(self.alphaSurf2, (620, 0))
        if self.gameOver == True:
            self.screen.blit(self.alphaSurf3, (200, 160))
        

        pygame.display.flip()

    #Play Game ######################################################
    def playLoop(self):

        #clock = pygame.time.Clock()

        #Main game loop #######################################
        while self.playing == True:
            
            if self.count == 1:
                self.bgMusic.play(-1)
            
            self.processEvents() 
            
            self.gameActions()

            self.displayScreen()

            self.clock.tick(100)
        
        if self.gameOver == True: #only if GO, not if exiting loop to menu
            self.bgMusic.stop()
        #######################################################
###############################################################