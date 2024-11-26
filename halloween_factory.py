# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
# Derived from https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/tree/main
#

import pygame
import os

from holiday_factory import HolidayFactory
from enemies.enemy import Enemy
from enemies.pumpkin import Pumpkin
from enemies.ghost import Ghost
from enemies.witch import Witch
from hero import Hero
from halloween_hero import HalloweenHero

ORANGE = (255, 165, 0)

class HalloweenFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(self, x, y) -> Enemy:
        return Pumpkin(x, y)

    def create_enemy_2(self, x, y) -> Enemy:
        return Ghost(x, y)

    def create_enemy_3(self, x, y) -> Enemy:
        return Witch(x, y)

    def create_enemy(self, type, x, y) -> Enemy:
        #print("Creating Halloween Enemy:")
        if type == 0:
            return Witch(x, y)
        elif type == 1:
            return Ghost(x, y)
        else:
            return Pumpkin(x, y)

    def create_hero(self, x, y, offset) -> Hero:
        return HalloweenHero(x, y, offset)

    def get_color(self):
        return ORANGE

    def print_info(self):
        print("I am the Halloween Factory")

    def get_background(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "halloween-background.png")
        splash_image = pygame.image.load(image_path)
        return splash_image

    def get_sound_path(self):
        sound_path = os.path.join("resources", "ghost_sound.ogg")
        return sound_path
