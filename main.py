#main

import pygame
from demo import GameLoop

game = GameLoop()

while game.running == True:  
    
    if game.gameOver == True: 
        game.__init__()

    game.curMenu.displayMenu()
    game.playLoop()

pygame.quit()