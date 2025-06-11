import pygame


pygame.init()
tela  = pygame.display.set_mode((300,300))


tela.fill((255,0,0))


pygame.display.flip()
         
run = True         
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run  = False
            pygame.quit()