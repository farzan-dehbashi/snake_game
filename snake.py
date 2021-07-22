import pygame
import sys
pygame.init()


#make the screen
screen = pygame.display.set_mode((500,500))
test_surface = pygame.Surface((100,100))
test_surface.fill(pygame.Color(0,0,200))
x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit() #closes any code that is running right now even if the pygame.quit is not completed that



    x_pos = x_pos +1
    screen.fill(pygame.Color(175,215,70))
    screen.blit(test_surface, (x_pos, 0))
    pygame.display.update() #update the screen
    pygame.time.Clock().tick(60) #60 frames per second