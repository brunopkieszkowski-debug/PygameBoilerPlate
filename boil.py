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
pygame.display.set_caption("FlappyBird")

#images
bloop = pygame.image.load('/home/bronu/pythons/pygame/sprites/Bloop.png').convert_alpha()


#Vars
squidx = 80
squidy = 100

#Classes
bloops = []
class Bloop:
    def __init__(self, color, x, y, size):
        self.color = color
        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        self.rect=pygame.draw.rect(win, self.color,((self.x,self.y),self.size))

    def move(self):
        self.y += 1.5

for count in range(5):
    for count in range(8):
        blooprect = back
        bloopsize = (50,50)
        bloops.append(Bloop(blooprect,squidx, squidy, bloopsize))
        squidx += 100
    squidx = 80
    squidy += 100

#Shapes


#main loop
run = True
while run:
    
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



    for Bloop in bloops:
        Bloop.draw()
        win.blit(bloop, ((Bloop.x-10),Bloop.y))
        #Bloop.move()
    pygame.display.update()
    clock.tick(60)
    win.fill(back)
pygame.quit()
os.system('cls')
sys.exit()
