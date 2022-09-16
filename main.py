import pygame
import random
import sys
from pygame.math import Vector2

class SNAKE:
    def __init__(self,screen, coin,cell_size,cell_number):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.snake_length=len(self.body)-3
        self.direction = Vector2(0, 0)
        self.new_block = False
        self.screen=screen
        self.coin=coin
        self.cell_size=cell_size
        self.cell_number=cell_number

        self.head_up = pygame.image.load('python ergasia/head_snake_UP (2).xcf').convert_alpha()
        self.head_down = pygame.image.load('python ergasia/head_snake_DOWN (2).xcf').convert_alpha()
        self.head_right = pygame.image.load('python ergasia/head_snake_RIGHT (2).xcf').convert_alpha()
        self.head_left = pygame.image.load('python ergasia/head_snake_LEFT (1).xcf').convert_alpha()
        self.tail = pygame.image.load('python ergasia/snake_tail.xcf').convert_alpha()

        self.tail_down = pygame.image.load('python ergasia/snake_tail_end_up.xcf').convert_alpha()
        self.tail_left = pygame.image.load('python ergasia/snake_tail_end_right.xcf').convert_alpha()
        self.tail_right = pygame.image.load('python ergasia/snake_tail_end_left.xcf').convert_alpha()
        self.tail_up = pygame.image.load('python ergasia/snake_tail_end_down.xcf').convert_alpha()

        self.body_horizontal = pygame.image.load('python ergasia/snake_tail_horizontal.xcf').convert_alpha()
        self.body_vertical = pygame.image.load('python ergasia/snake_tail_vertical.xcf').convert_alpha()

        self.body_tr = pygame.image.load('python ergasia/snake_tail_up_right.xcf').convert_alpha()
        self.body_tl = pygame.image.load('python ergasia/snake_tail_left_up.xcf').convert_alpha()
        self.body_br = pygame.image.load('python ergasia/snake_tail_right_down.xcf').convert_alpha()
        self.body_bl = pygame.image.load('python ergasia/snake_tail_left_down.xcf').convert_alpha()


    def draw_snake(self):
            self.update_head()
            self.update_tail()

            for index, block in enumerate(self.body):
                x_pos = int(block.x * self.cell_size)
                y_pos = int(block.y * self.cell_size)
                block_rect = pygame.Rect(x_pos, y_pos, self.cell_size, self.cell_size)

                if index == 0:
                    self.screen.blit(self.head, block_rect)  #displays the head of the snake
                elif index == len(self.body) - 1:
                    self.screen.blit(self.tail, block_rect)  #displays the tail of the snake
                else:                                        #displays the body of the snake
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.x == next_block.x:
                        self.screen.blit(self.body_vertical, block_rect)
                    elif previous_block.y == next_block.y:
                        self.screen.blit(self.body_horizontal, block_rect)
                    else:
                        if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                            self.screen.blit(self.body_tl, block_rect)
                        elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                            self.screen.blit(self.body_bl, block_rect)
                        elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                            self.screen.blit(self.body_tr, block_rect)
                        elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                            self.screen.blit(self.body_br, block_rect)


    def update_head(self):   #snake's head direction
            head_pl = self.body[1] - self.body[0]
            if head_pl == Vector2(1, 0):
                self.head = self.head_left
            elif head_pl == Vector2(-1, 0):
                self.head = self.head_right
            elif head_pl == Vector2(0, 1):
                self.head = self.head_up
            elif head_pl == Vector2(0, -1):
                self.head = self.head_down


    def update_tail(self):   #snake's tail direction
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


    def add_block(self):   #increases snake's length
        self.new_block = True


    def reset(self):   #brings the snake's length back to the initial length
            self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
            self.direction = Vector2(0, 0)

class COIN:
    def __init__(self,screen,image_coin,cell_size,cell_number):
        self.randomize()
        self.screen = screen
        self.image_coin = image_coin
        self.cell_size = cell_size
        self.cell_number = cell_number

    def draw_coin(self):   #displayw the coin
        coin_rect = pygame.Rect(self.pos.x*self.cell_size,self.pos.y*self.cell_size, self.cell_size, self.cell_size)
        self.screen.blit(self.image_coin,coin_rect)

    def randomize(self):   #coin's position
        self.x = random.randint(0,17)
        self.y = random.randint(0, 17)
        self.pos = Vector2(self.x, self.y)

class ENEMY2:
    def __init__(self,screen,image_enemy,cell_size,cell_number):
        self.randomize_enemy2()
        self.screen=screen
        self.image_enemy=image_enemy
        self.cell_size=cell_size
        self.cell_number=cell_number

    def draw_enemy2(self):   #displays the enemy
        enemy_rect=pygame.Rect(self.pos2.x*self.cell_size,self.pos2.y*self.cell_size, self.cell_size, self.cell_size)
        self.screen.blit(self.image_enemy,enemy_rect)

    def randomize_enemy2(self):  #enemy's position
        self.x2 = random.randint(0,17)
        self.y2 = random.randint(0, 17)
        self.pos2 = Vector2(self.x2, self.y2)

    def reset_enemy2(self):
        self.x= self.cell_size*self.cell_number+1
        self.y= self.cell_size*self.cell_number+1


class ENEMY:
    def __init__(self, screen, image_enemy, cell_size, cell_number):
        self.randomize_enemy()
        self.screen = screen
        self.image_enemy = image_enemy
        self.cell_size = cell_size
        self.cell_number = cell_number

    def draw_enemy(self):  #displays the enemy
        enemy_rect = pygame.Rect(self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size)
        self.screen.blit(self.image_enemy, enemy_rect)

    def randomize_enemy(self):    #enemy's position
        self.x = random.randint(0, 17)
        self.y = random.randint(0, 17)
        self.pos = Vector2(self.x, self.y)

    def reset_enemy(self):
        self.x= self.cell_size*self.cell_number+1
        self.y= self.cell_size*self.cell_number+1



class MAIN:
    def __init__(self,screen, image_coin,image_enemy,cell_size,cell_number,game_font):
        self.screen = screen
        self.image_coin = image_coin
        self.image_enemy=image_enemy
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.game_font=game_font
        self.snake = SNAKE(self.screen, self.image_coin,self.cell_size,self.cell_number)
        self.coin = COIN(self.screen, self.image_coin,self.cell_size,self.cell_number)
        self.enemy=ENEMY(self.screen, self.image_enemy,self.cell_size,self.cell_number)
        self.enemy2=ENEMY2(self.screen, self.image_enemy, self.cell_size, self.cell_number)
        self.coin_counter=0

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.failure()

    def draw_stuff(self):    #displays snake,coins,enemies and the background
        self.make_grass()
        self.coin.draw_coin()
        self.snake.draw_snake()
        self.scoreboard()
        if self.coin_counter==0:
            self.enemy.reset_enemy()
            self.enemy2.reset_enemy2()
        elif self.coin_counter%2!=1 and self.coin_counter>=7:   #displays enemies based on the score
            self.enemy.randomize_enemy()
        elif self.coin_counter%2!=1 and self.coin_counter>16:
            self.enemy.randomize_enemy()
            self.enemy2.randomize_enemy2()
        else:
            if self.coin_counter>=8 and self.coin_counter<12:
                self.enemy.draw_enemy()
            elif self.coin_counter==14:
                self.enemy.draw_enemy()
            elif self.coin_counter>14 and self.coin_counter<=16:
                self.enemy.draw_enemy()
            elif self.coin_counter > 14 and self.coin_counter <= 16:
                self.enemy.draw_enemy()
            elif self.coin_counter>16 and self.coin_counter<=18:
                self.enemy.draw_enemy()
                self.enemy2.draw_enemy2()
            elif self.coin_counter>18 and self.coin_counter<=20:
                self.enemy.draw_enemy()
                self.enemy2.draw_enemy2()
            elif self.coin_counter>20 and self.coin_counter<=22:
                self.enemy.draw_enemy()
                self.enemy2.draw_enemy2()
            elif self.coin_counter>22 and self.coin_counter<=24:
                self.enemy.draw_enemy()
                self.enemy2.draw_enemy2()
            elif self.coin_counter>24 and self.coin_counter<=26:
                self.enemy.draw_enemy()
                self.enemy2.draw_enemy2()
            elif self.coin_counter>26:
                self.enemy.draw_enemy()
                self.enemy2.draw_enemy2()

    def collision(self):    #detects collision between the snake and the coins
        if self.coin.pos == self.snake.body[0]:
            self.coin.randomize()
            self.snake.add_block()
            self.coin_counter=self.coin_counter+1  #increases the score

        for block in self.snake.body[1:]:          #increases snake's length
            if block == self.coin.pos:
                self.coin.randomize()

    def failure(self):   #if the snake collides with itself,the window or with an enemy the game is over
        if not 0 <= self.snake.body[0].x < self.cell_number or not 0 <= self.snake.body[0].y < self.cell_number:
            self.game_over()
        if self.enemy.pos==self.snake.body[0] or self.enemy2.pos2==self.snake.body[0]:
            self.game_over()
            self.enemy.randomize_enemy()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.coin_counter = 0

    def make_grass(self):    #displays the background
        #grass_color = (167,209,61)
        if (len(self.snake.body))-3< 8:  #level 1 background
            grass_color=(167,209,61)
            grass_color2=(175, 215, 70)
            clock.tick(80)
        elif (len(self.snake.body)-3)<=15:  #level 2 background
            grass_color=(221,211,255)
            grass_color2=(196,200,255)
        else:                              #level 3 background
            grass_color=(233,173,165)
            grass_color2=(255,216,173)

        for row in range(self.cell_number):
            if row % 2 == 0 :
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*self.cell_size,row*self.cell_size,self.cell_size,self.cell_size)
                        pygame.draw.rect(self.screen,grass_color,grass_rect)
                    else:
                        grass_rect = pygame.Rect(col*self.cell_size,row*self.cell_size,self.cell_size,self.cell_size)
                        pygame.draw.rect(self.screen, grass_color2, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
                    else:
                        grass_rect = pygame.Rect(col*self.cell_size,row*self.cell_size,self.cell_size,self.cell_size)
                        pygame.draw.rect(self.screen, grass_color2, grass_rect)

    def scoreboard(self):    #displas the scoreboard
        score_text =str(len(self.snake.body)- 3)
        score_surface = self.game_font.render(score_text,True,(56,74,12))
        sc_x =self.cell_size*self.cell_number -60
        sc_y = self.cell_size * self.cell_number - 40
        score_rect = score_surface.get_rect(center= (sc_x,sc_y))
        coin_rect = self.image_coin.get_rect(midright=(score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(coin_rect.left,coin_rect.top,coin_rect.width + score_rect.width + 10,coin_rect.height)

        pygame.draw.rect(self.screen,(167,209,61),bg_rect)
        self.screen.blit(score_surface,score_rect)
        self.screen.blit(self.image_coin,coin_rect)
        pygame.draw.rect(self.screen,(56,74,12),bg_rect,2)


#main code
pygame.init()
cell_size = 35 #40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
coin = pygame.image.load('python ergasia/coin (2).xcf').convert_alpha()
enemy=pygame.image.load('python ergasia/fence_pixel.xcf').convert_alpha()
game_font = pygame.font.Font(None, 25)

SCREEN_UPDATE = pygame.USEREVENT

main_game = MAIN(screen, coin,enemy,cell_size,cell_number,game_font)

pygame.time.set_timer(SCREEN_UPDATE, 200)

while True:
    ticks =pygame.time.get_ticks()
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
