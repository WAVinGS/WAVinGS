import threading
import time
import pygame
from pygame.locals import *
import numpy as np

# choose where to get started to degrade
def add_new(lst_degrade, w_, h_):
    """
    add random location into lst_degrade
    lst_degrade is used to check where ice has to degrade til becoming water
    """
    times = 1
    for i in range(times):
        w = np.random.randint(0, w_)
        h = np.random.randint(0, h_)
        if not (w, h) in lst_degrade:
            lst_degrade.append((w, h))

# used to change ice level
def degrade(matrix, lst_degrade):
    """
    degrade where ice has to degrade
    """
    for t in lst_degrade:
        matrix[t[0]][t[1]] = ice_degrade(matrix[t[0]][t[1]])

def ice_degrade(n):
    if n == 0: # 0 : complete
        return 3 # 3 : half-complete
    elif n == 3:
        return 1 # 1 : water
    # rock and water
    return n

# check if GG
def Is_GG(player_pos, block_size, matrix):
    w = round(player_pos[0] / block_size)
    h = round(player_pos[1] / block_size)
    if matrix[w][h] == 1:
        return True
    else:
        return False

def ini_background(matrix, width, height, block_size, offset):
    """
    draw background
    offset: used to move background
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                screen.blit(ice, (i*block_size-offset, j*block_size))
            elif matrix[i][j] == 1:
                screen.blit(water, (i*block_size-offset, j*block_size))
            elif matrix[i][j] == 2:
                screen.blit(rock, (i*block_size-offset, j*block_size))
            elif matrix[i][j] == 3:
                screen.blit(usumizu, (i*block_size-offset, j*block_size))

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

def map_update(matrix, offset, block_size, lst_degrade):
    """
    update new map(matrix)
    only when offset is same with block size, update map
    """
    if offset == block_size:
        # update matrix
        # lst is a random last column
        lst = []
        for i in range(len(matrix[0])):
            lst.append(possibility())
        matrix.append(lst)
        matrix.pop(0)

        # move degrading ice to left
        if any(lst_degrade):
            for i in range(len(lst_degrade)):
                if lst_degrade[i][0] <= 0:
                    lst_degrade.pop(i)
                else:
                    lst_degrade[i] = (lst_degrade[i][0]-1, lst_degrade[i][1])

        return 0
    return offset



pygame.init()

# img size
block_size = 80
w, h = 8, 6
width, height = block_size * w, block_size * h
screen = pygame.display.set_mode((width, height))

# load img
player = pygame.image.load("img/pixel-80x80.png")
ice = pygame.image.load("img/ice.png")
water = pygame.image.load("img/water.png")
rock = pygame.image.load("img/pixel-80x80.png")
usumizu = pygame.image.load("img/usumizu.png")


keys = [False, False, False, False]
width_mid = int(width/2 - block_size/2)
height_mid = int(height/2 - block_size/2)
player_pos = [width_mid, height_mid]
speed = 5
matrix = [[0 for i in range(h)] for j in range(w+1)]
matrix[4][3] = matrix[3][3] = matrix[4][2] = matrix[3][2] = 2
offset = 0


tmp = time.time()
lst_degrade = []

while True:
    # every 2 second make a degradation
    if time.time() - tmp > 5:
        tmp = time.time()
        add_new(lst_degrade, w, h)
        degrade(matrix, lst_degrade)

    # check if GG
    if Is_GG(player_pos, block_size, matrix):
        exit(55)

    screen.fill(0)

    # update matrix(map)
    offset = map_update(matrix, offset, block_size, lst_degrade)

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
        else:
            player_pos[1] -= speed
