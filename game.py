# CPSC 8700
# Project
#
# game.py
# contains came state, logic, and all elements

import pdb
import pygame
import random


import holiday_factory
from hero import Hero
from obstacle import Obstacle
from obstacle import grid
from enemies.enemy import Enemy
from holiday_factory import HolidayFactory
from laser import Laser

NUM_OBSTACLES = 4

class Game:
    def __init__(self, screen_width, screen_height, selected_holiday_factory):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.enemies_direction = 1
        self.selected_holiday_factory = selected_holiday_factory
        #print(f"Provided Factory: {self.selected_holiday_factory}")
        self.selected_holiday_factory.print_info()
        self.hero_group = pygame.sprite.GroupSingle() #this is like an inherent singleton
        #TODO:  make Hero a singleton and do getInstance()
        self.hero_group.add(Hero(self.screen_width, self.screen_height))
        self.obstacles = self.create_obstacles()
        self.enemies_group = pygame.sprite.Group()
        self.enemy_lasers_group = pygame.sprite.Group()
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
                x = 75 + column * 55
                y = 110 + row * 55
                if row == 0:
                    enemy = self.selected_holiday_factory.create_enemy(2, x, y)
                elif row in (1,2):
                    enemy = self.selected_holiday_factory.create_enemy(1, x, y)
                if row in (3,4):
                    enemy = self.selected_holiday_factory.create_enemy(0, x, y)
                self.enemies_group.add(enemy)
                #print(f"Created enemy: {enemy}")

    # This function moves the enemies left and right, each time a side is touched reverse direction, and move down
    def move_enemies(self):
        if self.enemies_group:
            self.enemies_group.update(self.enemies_direction)
        # get all enemy sprites
        enemy_sprites = self.enemies_group.sprites()
        for enemy_sprite in enemy_sprites:
            # check if any sprite has touched the side, if so change direction
            if enemy_sprite.rect.right > self.screen_width:
                self.enemies_direction = -1 # go left
                # TODO:  increasing this or scaling will increase the movement and difficulty
                self.move_enemies_down(2)
            if enemy_sprite.rect.left < 0:
                self.enemies_direction = 1 # go right
                self.move_enemies_down(2)


    def move_enemies_down(self, distance):
        # check if there are enemies on the screen
        if self.enemies_group:
            for enemy in self.enemies_group.sprites():
                # remember 0,0 is the top left so adding to y moves down
                enemy.rect.y += distance


    def shoot_enemy_laser(self):
        # check for existance of enemies
        if self.enemies_group.sprites():
            random_enemy = random.choice(self.enemies_group.sprites())
            laser_sprite = Laser(random_enemy.rect.center, -6, self.screen_height)
            self.enemy_lasers_group.add(laser_sprite)
