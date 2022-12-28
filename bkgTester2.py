#tester2

import pygame

#Screen
DISPLAY_W = 800
DISPLAY_H = 600
screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))

bkgSurface1 = pygame.Surface((DISPLAY_W // 2, DISPLAY_H))
bkgSurface2 = pygame.Surface((DISPLAY_W // 2, DISPLAY_H))

alpha = 25
alphaSurface = pygame.Surface((100, 100), flags=pygame.SRCALPHA)
white = (255, 255, 255)
gray = (150, 150, 150)

clock = pygame.time.Clock()

running = True

time = 10
count = 0

text2 = 'BKG Test'

def reduceTime(time):
    
    if count % 56 == 0:
        time -= 1

    if time == 0:
        time = 10
        
    return time

def delChar(text2):

    if count % 70 == 0:
        text2 = text2.rstrip(text2[-1])

    if text2 == '':
        text2 = 'BKG Test'

    return text2

def printText(font, text, color, pos, x, y):
        
        font = font
        text = font.render(text, True, color)
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

        alphaSurface.blit(text, textRect)

#Running loop
while running == True:

    pygame.init()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    text = 'Time:' + str(time)
    
    
    font = pygame.font.SysFont('OCR A Extended', 16)

    printText(font, text2, white, 'center', 50, 35)
    printText(font, text, white, 'center', 50, 65)

    time = reduceTime(time)
    text2 = delChar(text2)

    screen.blit(bkgSurface1, (DISPLAY_W // 2, 0))
    screen.blit(bkgSurface2, (0, 0))
    screen.blit(alphaSurface, (350, 250))
    bkgSurface1.fill(pygame.Color(150, 200, 75))
    bkgSurface2.fill(pygame.Color(0, 0, 0))
    alphaSurface.fill(pygame.Color(255, 255, 255, alpha))
    pygame.display.flip()

    count += 1
    clock.tick(100)

