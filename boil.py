import pygame
import sys
import os
from pygame.locals import *

pygame.init()

#Colors
back = (40,19,13)
red = (255, 51, 51)
white = (255,255,255)
orange = (255,102,51)
yellow = (255,192,51)
green = (151,255,51)
teal = (51,255,137)
ballcol = white

#Fonts
Big_font = pygame.font.Font("freesansbold.ttf", 60)
#Win
clock = pygame.time.Clock()
winw, winh = 900, 700
win = pygame.display.set_mode((winw,winh))
pygame.display.set_caption("GameTitle")

#images


#Vars

#Classes

#Shapes


#main loop
run = True
while run:
    
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    pygame.display.update()
    clock.tick(60)
    win.fill(back)
pygame.quit()
os.system('cls')
sys.exit()
