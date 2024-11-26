# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
# Derived from https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/tree/main
#

import pygame
import os

from hero import Hero
from holiday_type import HolidayType

# TODO:  Make Abstract and define specific Heros per holiday
class ChristmasHero(Hero):
    def __init__(self, screen_width, screen_height, offset):
        super().__init__(screen_width, screen_height, offset)
        image_path = os.path.join("resources", "green-hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=((self.screen_width + self.offset) / 2, self.screen_height)
        )  # middle and bottom
        self.holiday = HolidayType.CHRISTMAS

