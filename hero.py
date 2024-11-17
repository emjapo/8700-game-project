import pygame
import os

from laser import Laser

HERO_SPEED = 6

LASER_GUN_DELAY = 300

# TODO:  Make Abstract and define specific Heros per holiday
class Hero(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        # TODO: refactor the below 2 lines
        self.makeHalloweenHero()
        self.speed = HERO_SPEED
        self.lasers_group = pygame.sprite.Group()
        # Attributes necessary to prevent overlapping lasers
        self.laser_gun_ready = True
        self.laser_fired_time = 0

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.laser_gun_ready:
            self.laser_gun_ready = False
            laser = Laser(self.rect.center, 5, self.screen_height, self.holiday)
            self.lasers_group.add(laser)
            self.laser_fired_time = pygame.time.get_ticks()

    # Constrain the hero to the screen or it will scroll off the screen
    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        elif self.rect.left < 0:
            self.rect.left = 0

    # Renables the the laser gun after a cooloff time to prevent a constant stream of laser bullets
    def recharge_laser_gun(self):
        if not self.laser_gun_ready:
            current_time = pygame.time.get_ticks()
            # if enough time has passed, the laser is ready
            if ( current_time - self.laser_fired_time >= LASER_GUN_DELAY):
                self.laser_gun_ready = True

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser_gun()

    def makeChristmasHero(self):
        self.holiday = "christmas"
        image_path = os.path.join("resources", "hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.screen_width / 2, self.screen_height)
        )  # middle and bottom

    def makeHalloweenHero(self):
        self.holiday = "halloween"
        image_path = os.path.join("resources", "hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.screen_width / 2, self.screen_height)
        )  # middle and bottom
        
    def makeThanksgivingHero(self):
        self.holiday = "thanksgiving"
        image_path = os.path.join("resources", "hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.screen_width / 2, self.screen_height)
        )  # middle and bottom