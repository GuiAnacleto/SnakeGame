"""
author: Guilherme Anacleto Ferreira
contact: guilhermeanacleto@hotmail.com
date: 07/07/2021
"""

#==========================PYTHON SNAKE GAME==========================#

import pygame
import random

# Starts pygame library
pygame.init()

# Def Colors what will be used in our code
red = (213, 50, 80)
blue = (50, 153, 213)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 102)

# Def Size of the GameScreen
screen_width = 600
screen_height = 400

# Initialize The Game Screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Def Screen Title
pygame.display.set_caption('Snake Game by GuiAnacleto')

# Def the GameClock
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Game font
font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 25)


def Score(score):
    value = score_font.render("Score: " + str(score), True, white)
    screen.blit(value, [0, 0])


def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(
        0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(
        0, screen_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("DEAD! Press C to Play Again or Q to Quit", red)
            Score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(
            screen, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        Score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
