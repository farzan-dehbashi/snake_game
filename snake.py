import pygame
import sys
pygame.init()


#make the screen
screen = pygame.display.set_mode((500,500)) #makes the screen

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if the cross is pressed
            sys.exit() #closes any code that is running right now even if the pygame.quit is not completed that

    pygame.display.update() #update the screen
    pygame.time.Clock().tick(60) #60 frames per second