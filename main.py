import pygame

pygame.init()
WIDTH = 900 
HEIGHT = 750

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Brookxat chess')
timer = pygame.time.Clock()
fps = 60

# game variables

#main game loop

run = True

while run :
    timer.tick(fps)
    screen.fill('dark gray')

    # events handling
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :run = False
    pygame.display.flip()
pygame.quit()