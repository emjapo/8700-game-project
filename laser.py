# CPSC 8700
# Fall 2024
# Project
# Derived from https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/tree/main
#

import pygame
import os
from holiday_type import HolidayType
# yellow
LASER_COLOR = (243, 216, 63)
LASER_WIDTH = 10
LASER_HEIGHT = 30

LASER_TIME = 0
LASER_DELAY = 300

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height, type):
        super().__init__()
        if type == HolidayType.CHRISTMAS:
            image_path = os.path.join("resources", "christmas_light.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LASER_WIDTH, LASER_HEIGHT))
        elif type == HolidayType.HALLOWEEN:
            image_path = os.path.join("resources", "candy_corn.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LASER_WIDTH, LASER_HEIGHT))
        elif type == HolidayType.THANKSGIVING:
            image_path = os.path.join("resources", "gravy_blob.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LASER_WIDTH, LASER_HEIGHT))
        else:
            self.image = pygame.Surface((4, 15))
            self.image.fill(LASER_COLOR)
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height
        sound_path = os.path.join("resources", "shooting-sound.wav")
        self.laser_sound = pygame.mixer.Sound(sound_path)

    def update(self):
        self.rect.y -=self.speed
        # destroy all laser objects when they go offscreen, otherwise they just proliferate
        # when changing to an image, use the image rect bounds
        if(self.rect.y > self.screen_height + LASER_HEIGHT) or (self.rect.y < 0):
            self.kill
