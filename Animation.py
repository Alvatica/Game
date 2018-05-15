from __future__ import print_function, division

import pygame, random, time
pygame.init()


FPS = 250 # frames per second setting
fpsClock = pygame.time.Clock()
WIDTH = 750
HEIGHT = 500
size = [WIDTH, HEIGHT]
DISPLAYSURF = pygame.display.set_mode(size)
IMAGE = pygame.image.load('pokemon_by_transkitten-d8ct0bv.png')
RED = [255, 0, 0]
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
finish = 0
# -- PLAYER -- #
direction = 0
my_position = 10
my_position2 = 20

# -- ENEMIES -- #
x = random.randint(0, WIDTH)
y = random.randint(0, HEIGHT)

rect = ""


def position(self,x,y):
        self.left = x
        self.right = y
while finish == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = 1
    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(IMAGE, (x, y))
    pygame.display.flip()
pygame.quit()
