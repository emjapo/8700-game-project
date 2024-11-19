# CPSC 8700
# Fall 2024
# Project
# Derived from https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/tree/main
#

import pygame
from pygame.examples import grid

BLOCK_COLOR = (243,216,63)
BLOCK_PIXEL_WIDTH = 3
BLOCK_PIXEL_HEIGHT = 3
class Block(pygame.sprite.Sprite):

    #x and y are the block positions
    def __init__(self, x, y):
        super().__init__()
        #pygame.Surface provides a canvas for pixel image
        self.image = pygame.Surface((BLOCK_PIXEL_WIDTH, BLOCK_PIXEL_HEIGHT)) # 3 pixels wide, 3 pixels tall, maybe move to constant
        #TODO:  change to factory built image block and color
        self.image.fill(BLOCK_COLOR)
        self.rect = self.image.get_rect(topleft = (x,y))


# grid defines the shape of the obstacle
#TODO:  Make the grid[] below be different shapes based on the holiday factory
grid = [
    [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
]

class Obstacle:

    def __init__(self, x, y):
        self.blocks_group = pygame.sprite.Group()
        # loop over all elements of the grid
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == 1:
                    pos_x = x + column * BLOCK_PIXEL_WIDTH
                    pos_y = y + row * BLOCK_PIXEL_HEIGHT
                    block = Block(pos_x, pos_y)
                    self.blocks_group.add(block)
