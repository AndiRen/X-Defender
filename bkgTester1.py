import pygame


pygame.init()

window_surface = pygame.display.set_mode((640, 480))

background_1 = pygame.Surface((320, 480))
background_1.fill(pygame.Color(20,170,20))
background_2 = pygame.Surface((320, 480))


intermediate_alpha_surface = pygame.Surface((640, 480), flags=pygame.SRCALPHA)
intermediate_alpha_surface.fill(pygame.Color(0, 0, 0, 50))

font = pygame.font.Font(None, 14)

font_surface = font.render('Text with alpha background', True, (255,255,255,255)) #pygame.Color
font_rect = font_surface.get_rect()
font_rect.center = (320, 240)
intermediate_alpha_surface.blit(font_surface, font_rect)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background_2.fill(pygame.Color(170,20,20))
    #window_surface.blit(background_1, (0, 0))
    window_surface.blit(background_2, (320, 0))
    window_surface.blit(intermediate_alpha_surface, (0, 0))
    
    pygame.display.update()