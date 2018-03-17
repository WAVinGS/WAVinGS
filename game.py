import time
import pygame
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("img/pixel-80x80.png")
block_size = 80

keys = [False, False]
player_pos = [width/2 - block_size/2, height/2 - block_size/2]

while True:
    screen.fill(0)
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
                keys[1]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False

    if keys[0]:
        player_pos[0] -= 5
    elif keys[1]:
        player_pos[0] += 5
