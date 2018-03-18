import time
import pygame
from pygame.locals import *
import numpy as np

def ini_background(matrix, width, height, block_size, offset):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                screen.blit(water, (i*block_size-offset, j*block_size))
            elif matrix[i][j] == 1:
                screen.blit(ice, (i*block_size-offset, j*block_size))
            elif matrix[i][j] == 2:
                screen.blit(rock, (i*block_size-offset, j*block_size))

def possibility():
    # set level
    # 80% ice
    # 10% water
    # 10% rock
    p = np.random.rand() * 100
    if 0 <= p < 80:
        return 0
    elif 80 <= p < 90:
        return 1
    else:
        return 2

def map_update(matrix, offset, block_size):
    if offset == block_size:
        # update matrix
        # lst is a random last column
        lst = []
        for i in range(len(matrix[0])):
            lst.append(possibility())
        matrix.append(lst)
        matrix.pop(0)
        print(matrix)
        return 0
    return offset

pygame.init()

# img size
block_size = 80
w, h = 8, 6
width, height = block_size * w, block_size * h
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("img/pixel-80x80.png")
ice = pygame.image.load("img/ice.png")
water = pygame.image.load("img/water.png")
rock = pygame.image.load("img/pixel-80x80.png")

keys = [False, False, False, False]
width_mid = int(width/2 - block_size/2)
height_mid = int(height/2 - block_size/2)
player_pos = [width_mid, height_mid]
speed = 5
matrix = [[0 for i in range(h)] for j in range(w+1)]
matrix[3][2] = 1
offset = 0

while True:
    screen.fill(0)

    # update matrix(map)
    offset = map_update(matrix, offset, block_size)

    # print background
    ini_background(matrix, w, h, block_size, offset)

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

    # move left
    if keys[0]:
        if player_pos[0] <= 0:
            player_pos[0] = 0
        else:
            player_pos[0] -= speed
    # move right
    elif keys[1]:
        if player_pos[0] < width_mid:
            player_pos[0] += speed
            if player_pos[0] > width_mid:
                player_pos[0] = width_mid
        else:
            offset += speed
    # move down
    if keys[2]:
        if player_pos[1] >= height - block_size:
            player_pos[1] = height - block_size
        else:
            player_pos[1] += speed
    # move up
    elif keys[3]:
        if player_pos[1] <= 0:
            player_pos[1] = 0
            print(player_pos[1])
        else:
            player_pos[1] -= speed
            print(player_pos[1])
