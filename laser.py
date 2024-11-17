import pygame
import os

# yellow
LASER_COLOR = (243, 216, 63)
LASER_WIDTH = 10
LASER_HEIGHT = 30

LASER_TIME = 0
LASER_DELAY = 300

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height, type):
        super().__init__()
        if type == "christmas":
            image_path = os.path.join("resources", "christmas_light.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LASER_WIDTH, LASER_HEIGHT))
        elif type == "halloween":
            image_path = os.path.join("resources", "candy_corn.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LASER_WIDTH, LASER_HEIGHT))
        else:
            image_path = os.path.join("resources", "gravy_blob.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (LASER_WIDTH, LASER_HEIGHT))
        # self.image = pygame.Surface((LASER_WIDTH, LASER_HEIGHT))
        # self.image.fill(LASER_COLOR)
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -=self.speed
        # destroy all laser objects when they go offscreen, otherwise they just proliferate
        # when changing to an image, use the image rect bounds
        if(self.rect.y > self.screen_height + LASER_HEIGHT) or (self.rect.y < 0):
            self.kill
