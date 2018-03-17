import time
import pygame
from pygame.locals import *

def ini_background(screen, matrix, width, height, block_size):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            screen.blit(water, (i*block_size, j*block_size))

pygame.init()

# img size
block_size = 80
w, h = 8, 6
width, height = block_size * w, block_size * h
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("img/pixel-80x80.png")
water = pygame.image.load("img/water.png")
ice = pygame.image.load("img/ice.png")

keys = [False, False, False, False]
player_pos = [width/2 - block_size/2, height/2 - block_size/2]

matrix = [[0 for i in range(h)] for j in range(w)]

while True:
    screen.fill(0)

    # print background
    ini_background(screen, matrix, w, h, block_size)
    
    screen.blit(player, player_pos)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() 
            exit(0) 

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True
            elif event.key == K_DOWN:
                keys[2] = True
            elif event.key == K_UP:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            elif event.key == pygame.K_RIGHT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_UP:
                keys[3] = False

    if keys[0]:
        player_pos[0] -= 5
    elif keys[1]:
        player_pos[0] += 5
    if keys[2]:
        player_pos[1] += 5
    elif keys[3]:
        player_pos[1] -= 5
