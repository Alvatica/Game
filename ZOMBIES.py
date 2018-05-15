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
x = 0
y= 0
rect = ""
def __init__(self):
        pygame.sprite.Sprite__init__(self, self.containers)
        self.image = pygame.image.load('pokemon_by_transkitten-d8ct0bv.png')
        self.rect = self.image.get_rect()
def Position(self,x,y):
        x == random.randrange(WIDTH, 0)
        y == random.randrange(0, HEIGHT)
        self.rect.left = x
        self.rect.right = y
while finish == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = 1
    DISPLAYSURF.blit(IMAGE, (x, y))
    DISPLAYSURF.fill(BLACK)
    pygame.display.flip()
pygame.quit()
