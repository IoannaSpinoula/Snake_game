import pygame
import time
import math
import random
from pygame import mixer
from pygame.locals import *

class coin:
    def __init__(self, model2):
        self.model2 = model2
        self.image_coin = pygame.image.load("python ergasia/coin.xcf")
        self.x = random.randint(50, 850)
        self.y = random.randint(50, 850)

    def draw(self):
        self.model2.blit(self.image_coin,(self.x,self.y))
        pygame.display.flip()

class snake_head:
    def __init__(self,model):
        self.model = model
        self.image_right = pygame.image.load("python ergasia/head_snake_RIGHT.xcf")
        self.image_left = pygame.image.load("python ergasia/head_snake_LEFT.xcf")
        self.image_up = pygame.image.load("python ergasia/head_snake_UP.xcf")
        self.image_down = pygame.image.load("python ergasia/head_snake_DOWN.xcf")
        self.direction = 'up'
        self.x = 595
        self.y = 640

    def draw(self,x):
        self.model.fill((110, 110, 5))
        self.model.blit(x, (self.x,self.y))
        pygame.display.flip()

    def move_up(self):
        self.direction = 'up'
        self.draw(self.image_up)


    def move_down(self):
        self.direction = 'down'
        self.draw(self.image_down)


    def move_right(self):
        self.direction = 'right'
        self.draw(self.image_right)


    def move_left(self):
        self.direction = 'left'
        self.draw(self.image_left)


    def auto_move(self):
        if self.direction == 'up':
            self.y -= 2
            self.draw(self.image_up)

        elif self.direction == 'down':
            self.y += 2
            self.draw(self.image_down)

        elif self.direction == 'right':
            self.x += 2
            self.draw(self.image_right)

        elif self.direction == 'left':
            self.x -= 2
            self.draw(self.image_left)

class Game:
    def __init__(self):
        self.image_up = pygame.image.load("python ergasia/head_snake_UP.xcf")
        pygame.init()
        self.display= pygame.display.set_mode((900, 900))
        self.snake_head = snake_head(self.display)
        self.snake_head.draw(self.image_up)
        self.coin = coin(self.display)
        self.coin.draw()

    

    def play(self):
        self.snake.automove()
        self.coin.draw()



    def run(self):
        direction="Y"
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT and direction=="Y":
                        self.snake_head.move_right()
                        direction="X"
                    elif event.key == K_LEFT and direction=="Y":
                        self.snake_head.move_left()
                        direction="X"
                    elif event.key == K_UP and direction=="X":
                        self.snake_head.move_up()
                        direction="Y"
                    elif event.key == K_DOWN and direction=="X":
                        self.snake_head.move_down()
                        direction="Y"
            self.snake_head.auto_move()
            self.coin.draw()
            time.sleep(0.015)




if __name__ == '__main__':
    game = Game()
    game.run()
