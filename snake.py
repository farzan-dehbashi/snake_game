import pygame
import sys
import time
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN

# Snake class manages the snake

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()

    def move_down(self):
        self.y += 10
        self.draw()
    
    def move_up(self):
        self.y -= 10
        self.draw()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

# Game class manages the panel of the game

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.BACK_COLOR = (110, 110, 5)
        self.surface = pygame.display.set_mode((1000,500)) #makes the screen
        self.surface.fill(self.BACK_COLOR)
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                if event.type == pygame.QUIT: #if the cross is pressed
                    sys.exit() #closes any code that is running right now even if the pygame.quit is not completed that

            pygame.display.update() #update the screen
            pygame.time.Clock().tick(60) #60 frames per second

            self.snake.walk()
            time.sleep(0.2)


if __name__ == '__main__':
    game = Game()
    game.run()

