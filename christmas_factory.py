# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
#

import pygame
import os

from holiday_factory import HolidayFactory
from enemies.enemy import Enemy
from enemies.santa import Santa
from enemies.present import Present
from enemies.reindeer import Reindeer

from hero import Hero
from christmas_hero import ChristmasHero

RED = (255, 0, 0)
CRIMSON_RED = (220, 20, 60)
CARDINAL_RED = (196, 30, 58)

class ChristmasFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(self, x, y) -> Enemy:
        return Santa(x, y)

    def create_enemy_2(self, x, y) -> Enemy:
        return Present(x, y)

    def create_enemy_3(self, x, y) -> Enemy:
        return Reindeer(x, y)
    def create_enemy(self, type, x, y) -> Enemy:
        #print("Creating Halloween Enemy:")
        if type == 0:
            return Reindeer(x, y)
        elif type == 1:
            return Present(x, y)
        else:
            return Santa(x, y)

    def create_hero(self, x, y, offset) -> Hero:
        return ChristmasHero(x, y, offset)

    def get_color(self):
        return CRIMSON_RED

    def print_info(self):
        print("I am the Christmas Factory")

    def get_background(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "christmas-background.png")
        splash_image = pygame.image.load(image_path)
        if splash_image is None:
            print("Error: Background image failed to load.")
        return splash_image

    def get_sound_path(self):
        sound_path = os.path.join("resources", "sleigh_bells.wav")
        return sound_path