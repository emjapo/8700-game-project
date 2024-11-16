import pygame

#yellow
LASER_COLOR = (243, 216, 63)
LASER_WIDTH = 4
LASER_HEIGHT = 15

LASER_TIME = 0
LASER_DELAY = 300

class Laser(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        #TODO could change color or change image based on factory and subclass laser
        self.image = pygame.Surface((LASER_WIDTH, LASER_HEIGHT))
        self.image.fill(LASER_COLOR)
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -=self.speed
        #destroy all laser objects when they go offscreen, otherwise they just proliferate
        #when changing to an image, use the image rect bounds
        if(self.rect.y > self.screen_height + LASER_HEIGHT) or (self.rect.y < 0):
            self.kill

