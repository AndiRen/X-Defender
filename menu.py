import pygame
import my_colors

class Menu():

    def __init__(self, game):
        self.game = game
        self.mid_w = self.game.DISPLAY_W // 2
        self.mid_h = self.game.DISPLAY_H // 2
        self.runDisplay = True
        self.cursorRect = pygame.Rect(0, 0, 20, 20)
        self.offset = -200
        self.font = pygame.font.SysFont('OCR A Extended', 40, False, False)
        self.font2 = pygame.font.SysFont('OCR A Extended', 55, True)
        #self.font = pygame.font.Font('media/8bit16.ttf', 20)#, False, False)
        #self.font2 = pygame.font.Font('media/8bit16.ttf', 40)#, True, False)
        self.waitCount = 0
        self.select = False
    
    def drawCursor(self):
        text = '*'
        self.game.printText(self.font, text, my_colors.white, 'center', self.cursorRect.x, self.cursorRect.y, 'bkg') #game
    
    def updateMenu(self):
        self.game.screen.blit(self.game.bkgSurface, (0, 0))
        pygame.display.flip()
        self.game.clearKeys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx = self.mid_w
        self.starty = self.mid_h -100
        self.optionsx = self.mid_w
        self.optionsy = self.mid_h -50
        self.creditsx = self.mid_w
        self.creditsy = self.mid_h + 0
        self.quitx = self.mid_w
        self.quity = self.mid_h + 50
        self.cursorRect.midtop = ((self.startx + self.offset), self.starty)
        self.startColor = my_colors.white
        self.optionsColor = my_colors.fadeGrey
        self.creditsColor = my_colors.fadeGrey
        self.quitColor = my_colors.fadeGrey

    def findCurrent(self):
        
        #code to change color of menu item to white if cursor on it
        menuPos = [(self.startx, self.starty), (self.optionsx, self.optionsy), (self.creditsx, self.creditsy), (self.quitx, self.quity)]
        for pos in menuPos:
            if (self.cursorRect.x, self.cursorRect.y) == pos:
                #return pos
                print('yes!')

    def displayMenu(self):

        self.findCurrent()

        self.runDisplay = True
        while self.runDisplay == True:
            self.game.processEvents()
            self.checkInput()
            self.game.bkgSurface.fill(my_colors.black)
        
            if self.game.count == 0:
                self.game.printText(self.font2, 'Main Menu', my_colors.white, 'center', self.mid_w, self.mid_h - 175, 'bkg')
                self.game.printText(self.font, 'Start Game', self.startColor, 'center', self.startx, self.starty, 'bkg')
                self.game.printText(self.font, 'Credits', self.creditsColor, 'center', self.creditsx, self.creditsy, 'bkg')
            else:
                self.game.printText(self.font2, 'Game Menu', my_colors.white, 'center', self.mid_w, self.mid_h - 175, 'bkg')
                self.game.printText(self.font, 'Resume Game', self.startColor, 'center', self.startx, self.starty, 'bkg')
                self.game.printText(self.font, 'Main Menu', self.creditsColor, 'center', self.creditsx, self.creditsy, 'bkg')
            self.game.printText(self.font, 'Music Options', self.optionsColor, 'center', self.optionsx, self.optionsy, 'bkg')
            self.game.printText(self.font, 'Quit', self.quitColor, 'center', self.quitx, self.quity, 'bkg')
            
            self.drawCursor()
            self.updateMenu()
    
    def moveCursor(self):
        
        if self.game.DOWN_KEY == True and self.runDisplay == True:
            if self.state == 'Start':
                self.cursorRect.midtop = ((self.optionsx + self.offset), self.optionsy)
                self.state = 'Options'
                self.startColor = my_colors.fadeGrey
                self.optionsColor = my_colors.white
            elif self.state == 'Options':
                self.cursorRect.midtop = ((self.creditsx + self.offset), self.creditsy)
                self.state = 'Credits/End'
                self.optionsColor = my_colors.fadeGrey
                self.creditsColor = my_colors.white
            elif self.state == 'Credits/End':
                self.cursorRect.midtop = ((self.quitx + self.offset), self.quity)
                self.state = 'Quit'
                self.creditsColor = my_colors.fadeGrey
                self.quitColor = my_colors.white    
            elif self.state == 'Quit':
                self.cursorRect.midtop = ((self.startx + self.offset), self.starty)
                self.state = 'Start'
                self.quitColor = my_colors.fadeGrey
                self.startColor = my_colors.white
        
        elif self.game.UP_KEY == True:
            if self.state == 'Start':
                self.cursorRect.midtop = ((self.quitx + self.offset), self.quity)
                self.state = 'Quit'
                self.startColor = my_colors.fadeGrey
                self.quitColor = my_colors.white
            elif self.state == 'Options':
                self.cursorRect.midtop = ((self.startx + self.offset), self.starty)
                self.state = 'Start'
                self.optionsColor = my_colors.fadeGrey
                self.startColor = my_colors.white
            elif self.state == 'Credits/End':
                self.cursorRect.midtop = ((self.optionsx + self.offset), self.optionsy)
                self.state = 'Options'
                self.creditsColor = my_colors.fadeGrey
                self.optionsColor = my_colors.white
            elif self.state == 'Quit':
                self.cursorRect.midtop = ((self.creditsx + self.offset), self.creditsy)
                self.state = 'Credits/End'
                self.quitColor = my_colors.fadeGrey
                self.creditsColor = my_colors.white
    
    def checkInput(self):
        self.moveCursor()
        if self.game.START_KEY == True:
            self.runDisplay = False
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curMenu = self.game.options
            elif self.state == 'Credits/End':
                if self.game.count == 0:
                    self.game.curMenu = self.game.credits
                else:
                    self.game.playing = False
                    self.game.gameOver = True
            elif self.state == "Quit":
                self.game.running = False
            #self.runDisplay = False 

class CreditsMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)  

    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay == True:
            self.game.processEvents()
            if self.game.BACK_KEY == True or self.game.START_KEY == True:
                self.game.curMenu = self.game.mainMenu
                self.runDisplay = False
            self.game.bkgSurface.fill(my_colors.black)
            self.game.printText(self.font, 'Game by @ndi Ren', my_colors.white, 'center', self.mid_w, self.mid_h - 150, 'bkg')
            self.game.printText(self.font, 'Music by FoolBoyMedia', my_colors.white, 'center', self.mid_w, self.mid_h - 50, 'bkg')
            self.game.printText(self.font, 'via freesound.org', my_colors.white, 'center', self.mid_w, self.mid_h + 0, 'bkg')
            self.updateMenu()

class OptionsMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'on'
        self.onx = self.mid_w
        self.ony = self.mid_h - 50
        self.offx = self.mid_w
        self.offy = self.mid_h
        self.cursorRect.midtop = ((self.onx + self.offset), self.ony)
        self.onColor = my_colors.white
        self.offColor = my_colors.fadeGrey
    
    def displayMenu(self):
        self.runDisplay = True
        while self.runDisplay == True:
            self.game.processEvents()
            self.checkInput()
            self.game.bkgSurface.fill(my_colors.black)
            self.game.printText(self.font2, 'Music Options', my_colors.white, 'center', self.mid_w, self.mid_h - 125, 'bkg')
            self.game.printText(self.font, 'On', self.onColor, 'center', self.onx, self.ony, 'bkg')
            self.game.printText(self.font, 'Off', self.offColor, 'center', self.offx, self.offy, 'bkg')
            self.drawCursor()
            self.updateMenu()
    
    def checkInput(self):
        
        self.moveCursor()
        
        if self.game.BACK_KEY == True:
            self.game.curMenu = self.game.mainMenu
            self.runDisplay = False
        elif self.game.START_KEY == True:
            if self.state == 'on':
                self.game.bgMusic.set_volume(0.3)
            elif self.state == 'off':
                self.game.bgMusic.set_volume(0.0)
            self.select = True
        
        #Wait timer for closing music menu after selecting volume level #####
        if self.select == True:
            self.waitCount += 1
            #print(self.waitCount)
        if self.waitCount == 750:
            self.select = False
            self.waitCount = 0
            self.game.curMenu = self.game.mainMenu
            self.runDisplay = False
        ######################################################################
        
    def moveCursor(self):
        if self.game.UP_KEY == True or self.game.DOWN_KEY == True:
            if self.state == 'on':
                self.state = 'off'
                self.cursorRect.midtop = ((self.offx + self.offset), self.offy)
                self.onColor = my_colors.fadeGrey
                self.offColor = my_colors.white
            elif self.state == 'off':
                self.state = 'on'
                self.cursorRect.midtop = ((self.onx + self.offset), self.ony)
                self.offColor = my_colors.fadeGrey
                self.onColor = my_colors.white

