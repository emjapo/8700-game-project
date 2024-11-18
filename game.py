# CPSC 8700
# Project
#
# game.py
# contains came state, logic, and all elements
# import

import pdb
import pygame
import random

from game_data import GameData

from holiday_type import HolidayType
from holiday_factory import HolidayFactory
from factory_selector import FactorySelector
from halloween_factory import HalloweenFactory
from thanksgiving_factory import ThanksgivingFactory
from christmas_factory import ChristmasFactory

from hero import Hero
from obstacle import Obstacle
from obstacle import grid
from enemies.enemy import Enemy
from laser import Laser

NUM_OBSTACLES = 4
ENEMY_LASER_FIRE_INTERVAL = 800 # 300ms between the firings of lasers from enemies, this could increase as dificulty increases

class Game:
    def __init__(self, screen_width, screen_height, offset):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset

        self.data = GameData()

        # Initial holiday is halloween
        #self.current_holiday_type = HolidayType.HALLOWEEN
        self.current_holiday_type = HolidayType.THANKSGIVING
        self.current_holiday_factory = FactorySelector.get_factory(self.current_holiday_type)
        print(f"Created Factory: {self.current_holiday_factory}")

        self.enemies_direction = 1

        self.hero_group = pygame.sprite.GroupSingle() #this is like an inherent singleton
        #TODO:  make Hero a singleton and do getInstance()
        self.hero = Hero(self.screen_width, self.screen_height, self.offset)
        self.hero_group.add(self.hero)
        self.obstacles = self.create_obstacles()
        self.enemies_group = pygame.sprite.Group()
        # Setup for the enemy laser firings
        self.enemy_lasers_group = pygame.sprite.Group()
        self.enemy_laser_event = pygame.USEREVENT
        pygame.time.set_timer(self.enemy_laser_event, ENEMY_LASER_FIRE_INTERVAL)
        self.running = True;

        self.create_enemies()

    def create_obstacles(self):
        # Want 4 obstacles
        obstacle_width = len(grid[0]) * 3 #TODO:  change 3 to Obstacle width
        obstacle_spacing = (self.screen_width + self.offset - (NUM_OBSTACLES * obstacle_width)) / (NUM_OBSTACLES+1)
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
                    enemy_type = 2
                elif row in (1,2):
                    enemy_type = 1
                else: # rows 3,4
                    enemy_type = 0
                enemy = self.current_holiday_factory.create_enemy(enemy_type, x + self.offset/2, y)
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
            if enemy_sprite.rect.right > self.screen_width + (self.offset/2):
                self.enemies_direction = -1 # go left
                # For Testing
                # self.enemies_direction = -40 # go left
                # TODO:  increasing this or scaling will increase the movement and difficulty
                self.move_enemies_down(2)
            if enemy_sprite.rect.left < self.offset / 2:
                self.enemies_direction = 1 # go right
                # For Tesging
                #self.enemies_direction = 40 # go right
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
            laser_sprite = Laser(random_enemy.rect.center, -6, self.screen_height, "enemy")
            self.enemy_lasers_group.add(laser_sprite)

    def check_for_collision(self):
        # Hero Lasers
        # Check if any of the "lasers" from the spaceships collided with an enemy
        if self.hero_group.sprite.lasers_group:
            for laser_sprite in self.hero_group.sprite.lasers_group:
                # returns a list of all collided sprites, but by setting the doKill bool to True this will send a kill() to the sprite
                # but you must then on having a successful collision also kill the laser fired or it will continue across the screen killing everying
                if pygame.sprite.spritecollide(laser_sprite, self.enemies_group, True):
                    laser_sprite.kill()
                # loop over the obstacles
                for obstacle in self.obstacles:
                    # like above on collision remove the laser
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
        # Enemy Lasers
        # if there are lasers from the enemies in the scene
        if self.enemy_lasers_group:
            for laser_sprite in self.enemy_lasers_group:
                # check for the collision with the hero BUT do not kill() the hero, the player will have multiple lives
                if pygame.sprite.spritecollide(laser_sprite, self.hero_group, False):
                    laser_sprite.kill()
                    print("Hero hit by laser")
                    self.hero.hit()
                    self.data.lives -= 1
                    #self.hero.decrease_lives()
                    #if self.hero.get_number_of_lives() == 0:
                    if self.data.lives == 0:
                            self.game_over()
                # loop over the obstacles and check that the enemy lasers have hit the obstacles
                for obstacle in self.obstacles:
                    # like above on collision remove the laser
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

        # Check for collisions between the enemies and the obstacles and hero
        if self.enemies_group: # are there current enemies
            for enemy in self.enemies_group:
                for obstacle in self.obstacles:
                    # must check against collision with each of the obstacles
                    pygame.sprite.spritecollide(enemy, obstacle.blocks_group, True)
                # check for collision with an enemy and the hero
                if pygame.sprite.spritecollide(enemy, self.hero_group, False):
                    self.hero.hit()
                    self.data.lives -= 1
                    #self.hero.decrease_lives()
                    if self.data.lives == 0:
                        self.game_over()
                    print("Hero hit by enemy")

    def check_for_enemies(self):
        if self.running:
            if len(self.enemies_group) == 0:
                print("No enemies")
                # No enemies on screen, so level complete
                self.running == False
                self.next_level()
                self.running == True

    def next_level(self):
        # do similar to reset
        # update lives, do we want to give some back?
        #self.data.lives = 3
        # Get the new holiday
        print(f"Holiday Type: {self.current_holiday_type}")
        if self.current_holiday_type == HolidayType.HALLOWEEN:
            self.current_holiday_type = HolidayType.THANKSGIVING
            print("Change to Thanksgiving")
        elif self.current_holiday_type == HolidayType.THANKSGIVING:
            self.current_holiday_type = HolidayType.CHRISTMAS
            print("Change to Christmas")
        elif self.current_holiday_type == HolidayType.CHRISTMAS:
            self.current_holiday_type = HolidayType.HALLOWEEN
            print("Change to Halloween")
        self.current_holiday_factory = FactorySelector.get_factory(self.current_holiday_type)
        # Hero will need to be updated to the new holiday
        self.hero_group.sprite.reset()
        self.enemies_group.empty()
        self.enemy_lasers_group.empty()
        self.create_enemies()
        self.create_obstacles()
        # TODO: adjust scoring and difficulty
        # TODO: Score could go up per level, and enemies can move faster and shoot more often
        self.data.level += 1
        print("Next level")


    def update(self):
        self.hero_group.update()
        self.move_enemies()
        # self.game.shoot_enemy_laser()
        self.enemy_lasers_group.update()
        self.check_for_collision()
        self.check_for_enemies()

    def render(self, screen):
        # TODO add in the background for each holiday level
        # Draw the hero shooter on the bottom
        self.hero_group.draw(screen)
        # Draw all the lasers of the hero
        self.hero_group.sprite.lasers_group.draw(screen)
        # self.hero_group.sprite.laser_group.draw(self.screen)
        for obstacle in self.obstacles:
            obstacle.blocks_group.draw(screen)
        self.enemies_group.draw(screen)

        # draw all the enemy lasers firing
        self.enemy_lasers_group.draw(screen)

    def game_over(self):
        print("Game Over!")
        self.running = False

    def reset(self):
        #reset game state
        self.data.lives = 3
        self.hero_group.sprite.reset()
        self.enemies_group.empty()
        self.enemy_lasers_group.empty()
        self.create_enemies()
        self.create_obstacles()
        self.running = True
    def get_level(self):
        return self.data.level

    def get_lives(self):
        return self.data.lives

    def get_high_score(self):
        return self.data.high_score

    def get_theme_color(self):
        return self.current_holiday_factory.get_color()

