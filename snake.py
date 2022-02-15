import pygame
import sys
import time
import random
from pygame.constants import K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, KEYDOWN

# Each tile of screen is 40 by 40 pixels

SIZE = 40

# Apple class represents prises the snake eats

class Apple:

    # Initialize apple at a random tile

    def __init__(self, parent_screen) -> None:
        self.image = pygame.image.load('resources/apple.jpg').convert()
        self.parent_screen = parent_screen
        self.x = random.randint(0,14) * SIZE
        self.y = random.randint(0,14) * SIZE

    # Draws the apple at it's location

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    # Relocates apple
    
    def relocate(self):
        self.x = random.randint(0,14) * SIZE
        self.y = random.randint(0,14) * SIZE


# Snake class manages the snake

class Snake:

    # Initiates the snake by size 2. And, initial direction of move to the right

    def __init__(self, parent_screen):
        self.length = 2
        self.parent_screen = parent_screen
        self.block = pygame.image.load('resources/block.jpg').convert()
        self.x = [random.randint(0,14) * SIZE] * self.length
        self.y = [random.randint(0,14) * SIZE] * self.length
        self.direction = 'right'

    # Draws snake and refreshes the parent display

    def draw(self):
        self.parent_screen.fill((80, 155, 50))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    # Moves snake to down by changing direction

    def move_down(self):
        self.direction = 'left'

    # Moves snake to up by changing direction
    
    def move_up(self):
        self.direction = 'up'
    
    # Moves snake to left by changing direction

    def move_left(self):
        self.direction = 'left'

    # Moves snake to right by changing direction

    def move_right(self):
        self.direction = 'right'

    # Manages the movement of the body of snake. Body follows the head.

    def walk(self):
        for i in range (self.length -1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'right':
            self.x[0] += SIZE
            self.x[0] %= 600
        if self.direction == 'left':
            self.x[0] -= SIZE
            if self.x[0] < 0:
                self.x[0] = 600
        if self.direction == 'up':
            self.y[0] -= SIZE
            if self.y[0] < 0:
                self.y[0] = 600
        if self.direction == 'down':
            self.y[0] += SIZE
            self.y[0] %= 600
        self.draw()
    
    # Increases the length of the snake

    def grow(self):
        self.length += 1
        self.x.append(-1) # grow one block
        self.y.append(-1)


# Game class manages the panel of the game

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.BACK_COLOR = (110, 110, 5)
        self.surface = pygame.display.set_mode((600,600)) #makes the screen
        self.surface.fill(self.BACK_COLOR)
        self.snake = Snake(self.surface)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    # Checks if two points match
    
    def is_collided(self, x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            return True
        else:
            return False
    
    # Updates panel

    def play(self):
        self.snake.walk()
        self.apple.draw()
        
    # When game over happens, it displays score and pauses the game.

    def display_game_over(self):
        font = pygame.font.SysFont('arial', 20)
        score = font.render(f'Score: {self.snake.length}', True, (200,200,200))
        self.surface.blit(score, (50, 50))
        game_over_message = font.render(f'Game over!', True, (200,200,200))
        self.surface.blit(game_over_message, (250, 300))
        pygame.display.flip()

    # Checks if the user is game over

    def game_over(self, snake):
        game_over = False
        if snake.x[0] in snake.x[1:] and snake.y[0] in snake.y[1:]:
            game_over = True
        return game_over

    # Core of the game to manage panel

    def run(self):
        running = True
        game_over = False
        while running:

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_UP:
                        self.snake.move_up()
                        self.snake.direction = 'up'
                    if event.key == K_DOWN:
                        self.snake.move_down()
                        self.snake.direction = 'down'
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                        self.snake.direction = 'right'
                    if event.key == K_LEFT:
                        self.snake.move_left()
                        self.snake.direction = 'left'
                if event.type == pygame.QUIT: #if the cross is pressed
                    sys.exit() #closes any code that is running right now even if the pygame.quit is not completed that
            
            if not game_over:
                pygame.display.update() #update the screen
                pygame.time.Clock().tick(60) #60 frames per second
                self.play()
                time.sleep(0.1)

            # Checks if collision of snake head and an apple happens

            if self.is_collided(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y): 
                self.apple.relocate()
                self.snake.grow()

            # Checks if the user is game over, pause the game and display proper message
            
            if self.game_over(self.snake): 
                game_over = True
                self.display_game_over()

   


if __name__ == '__main__':
    game = Game()
    game.run()

