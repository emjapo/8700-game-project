import pygame
import os

from holiday_factory import HolidayFactory
from enemies.enemy import Enemy
from enemies.turkey import Turkey
from enemies.corn import Corn
from enemies.macaroni import Macaroni

from hero import Hero
from thanksgiving_hero import ThanksgivingHero

BROWN = (139, 69, 19)

class ThanksgivingFactory(HolidayFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_enemy_1(self, x, y) -> Enemy:
        return Turkey(x, y)

    def create_enemy_2(self, x, y) -> Enemy:
        return Corn(x, y)

    def create_enemy_3(self, x, y) -> Enemy:
        return Macaroni(x, y)

    def create_enemy(self, type, x, y) -> Enemy:
        #print("Creating Halloween Enemy:")
        if type == 0:
            return Macaroni(x, y)
        elif type == 1:
            return Corn(x, y)
        else:
            return Turkey(x, y)

    def create_hero(self, x, y, offset) -> Hero:
        return ThanksgivingHero(x, y, offset)

    def get_color(self):
        return BROWN

    def print_info(self):
        print("I am the Thanksgiving Factory")

    def get_background(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "thanksgiving-background.png")
        try:
            splash_image = pygame.image.load(image_path)
            #splash_image.convert_alpha()
            #splash_image.set_alpha(22)
        except pygame.error as e:
            print(f"Error loading Thanksgiving background image: {e}")
        return splash_image

    def get_sound_path(self):
        sound_path = os.path.join("resources", "turkey_gobble.wav")
        return sound_path
