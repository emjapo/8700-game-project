# CPSC 8700
# Project
#
# game.py
# contains came state, logic, and all elements

import pygame

from hero import Hero
from obstacle import Obstacle
from obstacle import grid

NUM_OBSTACLES = 4

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.hero_group = pygame.sprite.GroupSingle() #this is like an inherent singleton
        #TODO:  make Hero a singleton and do getInstance()
        self.hero_group.add(Hero(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacles()

    def create_obstacles(self):
        # Want 4 obstacles
        obstacle_width = len(grid[0]) * 3 #TODO:  change 3 to Obstacle width
        obstacle_spacing = (self.screen_width - (NUM_OBSTACLES * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            print("i: " + str(i))
            offset_x = (i + 1) * obstacle_spacing + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles

