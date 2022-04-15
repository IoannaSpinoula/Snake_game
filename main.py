import pygame
import random
import sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('python ergasia/head_snake_UP.xcf').convert_alpha()
        self.head_down = pygame.image.load('python ergasia/head_snake_DOWN.xcf').convert_alpha()
        self.head_right = pygame.image.load('python ergasia/head_snake_RIGHT.xcf').convert_alpha()
        self.head_left = pygame.image.load('python ergasia/head_snake_LEFT(1).xcf').convert_alpha()
        self.tail = pygame.image.load('python ergasia/snake_tail.xcf').convert_alpha()

        self.tail_down = pygame.image.load('python ergasia/snake_tail_end_up.xcf').convert_alpha()
        self.tail_left = pygame.image.load('python ergasia/snake_tail_end_right.xcf').convert_alpha()
        self.tail_right = pygame.image.load('python ergasia/snake_tail_end_left.xcf').convert_alpha()
        self.tail_up = pygame.image.load('python ergasia/snake_tail_end_down.xcf').convert_alpha()

        self.body_horizontal = pygame.image.load('python ergasia/snake_tail_horizontal.xcf').convert_alpha()
        self.body_vertical = pygame.image.load('python ergasia/snake_tail_vertical.xcf').convert_alpha()

        self.body_tr = pygame.image.load('python ergasia/snake_tail_up_right.xcf').convert_alpha()
        self.body_tl = pygame.image.load('python ergasia/snake_tail_left_up.xcf').convert_alpha()
        self.body_br =pygame.image.load('python ergasia/snake_tail_right_down.xcf').convert_alpha()
        self.body_bl = pygame.image.load('python ergasia/snake_tail_left_down.xcf').convert_alpha()

    def draw_snake(self):
        self.update_head()
        self.update_tail()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head(self):
        head_pl = self.body[1] - self.body[0]
        if head_pl == Vector2(1,0):
            self.head = self.head_left
        elif head_pl == Vector2(-1,0):
            self.head = self.head_right
        elif head_pl == Vector2(0,1):
            self.head = self.head_up
        elif head_pl == Vector2(0,-1):
            self.head = self.head_down

    def update_tail(self):
        tail_pl = self.body[-2] - self.body[-1]
        if tail_pl == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_pl == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_pl == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_pl == Vector2(0, -1):
                self.tail = self.tail_down


    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

class COIN:
    def __init__(self):
        self.randomize()

    def draw_coin(self):
        coin_rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size, cell_size, cell_size)
        screen.blit(coin,coin_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.coin = COIN()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.failure()

    def draw_stuff(self):
        self.make_grass()
        self.coin.draw_coin()
        self.snake.draw_snake()
        self.scoreboard()

    def collision(self):
        if self.coin.pos == self.snake.body[0]:
            self.coin.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.coin.pos:
                self.coin.randomize()

    def failure(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def make_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row % 2 == 0 :
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def scoreboard(self):
        score_text =str(len(self.snake.body)- 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        sc_x =cell_size*cell_number -60
        sc_y = cell_size * cell_number - 40
        score_rect = score_surface.get_rect(center= (sc_x,sc_y))
        coin_rect = coin.get_rect(midright=(score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(coin_rect.left,coin_rect.top,coin_rect.width + score_rect.width + 10,coin_rect.height)

        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(coin,coin_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)

pygame.init()
cell_size = 35
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
coin = pygame.image.load('python ergasia/coin.xcf').convert_alpha()
game_font = pygame.font.Font(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_stuff()
    pygame.display.update()


    clock.tick(60)
