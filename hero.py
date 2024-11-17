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
        # TODO: modify with private scoping via _
        self.number_of_lives = 3
        sound_path = os.path.join("resources", "hit-sound.wav")
        self.hit_sound = pygame.mixer.Sound(sound_path)

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE] and self.laser_gun_ready:
            self.laser_gun_ready = False
            laser = Laser(self.rect.center, 5, self.screen_height, self.holiday)
            laser.laser_sound.play()
            self.lasers_group.add(laser)
            self.laser_fired_time = pygame.time.get_ticks()

    # Constrain the hero to the screen, or it will scroll off the screen
    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        elif self.rect.left < 0:
            self.rect.left = 0

    # Renables the the laser gun after a cool-off time to prevent a constant stream of laser bullets
    def recharge_laser_gun(self):
        if not self.laser_gun_ready:
            current_time = pygame.time.get_ticks()
            # if enough time has passed, the laser is ready
            if ( current_time - self.laser_fired_time >= LASER_GUN_DELAY):
                self.laser_gun_ready = True

    def decrease_lives(self):
        self.number_of_lives -= 1
        self.hit_sound.play()

    def get_number_of_lives(self):
        return self.number_of_lives

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser_gun()

    def reset(self):
        self.rect = self.image.get_rect(midbottom = (self.screen_width / 2, self.screen_height))
        self.lasers_group.empty()

    def makeChristmasHero(self):
        self.holiday = "christmas"
        image_path = os.path.join("resources", "green-hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.screen_width / 2, self.screen_height)
        )  # middle and bottom

    def makeHalloweenHero(self):
        self.holiday = "halloween"
        image_path = os.path.join("resources", "orange-hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.screen_width / 2, self.screen_height)
        )  # middle and bottom

    def makeThanksgivingHero(self):
        self.holiday = "thanksgiving"
        image_path = os.path.join("resources", "red-hero.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(
            midbottom=(self.screen_width / 2, self.screen_height)
        )  # middle and bottom
