# CPSC 8700
# Project
#
# game.py
# contains came state, logic, and all elements

import pygame

import holiday_factory
from hero import Hero
from obstacle import Obstacle
from obstacle import grid
from enemies.enemy import Enemy
from holiday_factory import HolidayFactory

NUM_OBSTACLES = 4

class Game:
    def __init__(self, screen_width, screen_height, selected_holiday_factory):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.selected_holiday_factory = selected_holiday_factory
        print(f"Provided Factory: {self.selected_holiday_factory}")
        print("What factory")
        self.selected_holiday_factory.print_info()
        print("did I get a factory")
        self.hero_group = pygame.sprite.GroupSingle() #this is like an inherent singleton
        #TODO:  make Hero a singleton and do getInstance()
        self.hero_group.add(Hero(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacles()
        self.enemies_group = pygame.sprite.Group()
        self.create_enemies()

    def create_obstacles(self):
        # Want 4 obstacles
        obstacle_width = len(grid[0]) * 3 #TODO:  change 3 to Obstacle width
        obstacle_spacing = (self.screen_width - (NUM_OBSTACLES * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * obstacle_spacing + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles

    def create_enemies(self):
        for row in range(5):
            for column in range(11):
                x = column * 55
                y = row * 55
                enemy = self.selected_holiday_factory.create_enemy(0, x, y)
                print(f"Created enemy: {enemy}")
                self.enemies_group.add(enemy)

