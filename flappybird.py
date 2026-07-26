import pygame
from pygame import *
from random import randint
from time import sleep


init()

window_size = 1200,800

window = display.set_mode(window_size)
clock = time.Clock()

player_rect = Rect(150, window_size[1]//2-100,100,100)

def generete_pipes(count,pipe_width = 140, gap=200,min_height=50,max_height=440,distance=650):
    pipes = []
    start_x = window_size[0]
    for i in range(count):
        height = randint(min_height,max_height)
        top_pipe = Rect(start_x,0,pipe_width,height)
        bottom_pipe = Rect(start_x,height + gap,pipe_width,height)
        pipes.extend([top_pipe,bottom_pipe])
        start_x += distance
    return pipes

pipes = generete_pipes(150)
main_font = font.Font(None, 100)

score = 0
lose = False
y_velocity = 2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

    window.fill("sky blue")
    draw.rect(window,"red",player_rect)
    for pipe in pipes:
        if not lose:
            pipe.x -= 10
        draw.rect(window,"green",pipe)
        if player_rect.colliderect(pipe):
            lose = True
    if len(pipes) <8:
        pipes += generete_pipes(150)

    score_text = main_font.render(f"{int(score)}", 1, "black")
    center_text = window_size[0]//2 - score_text.get_rect().w
    window.blit(score_text,(center_text, 40))

    display.update()
    clock.tick(60)


    keys = key.get_pressed()

    if keys[K_w] and not lose: player_rect.y -= 10
    if keys[K_s] and not lose: player_rect.y += 10
    if keys[K_r] and lose:
        lose = False
        score = 0
        pipes = generete_pipes(150)
        player_rect.y = window_size[1]//2-100
        y_velocity = 2

    if player_rect.y >= window_size[1] - player_rect.h: lose = True
    if lose:
        player_rect.y += y_velocity
        y_velocity *= 1.1




