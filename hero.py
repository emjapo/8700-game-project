import pygame
import os

HERO_SPEED = 6

#TODO:  Make Abstract and define specific Heros per holiday
class Hero(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        #TODO: refactor the below 2 lines
        image_path = os.path.join('resources', 'hero.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2,self.screen_height)) #middle and bottom
        self.speed = HERO_SPEED


    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
           self.rect.x -= self.speed
        elif keys[pygame.K_RIGHT]:
           self.rect.x += self.speed

    #Constrain the hero to the screen or it will scroll off the screen
    def constrain_movement(self):
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        elif self.rect.left < 0:
            self.rect.left = 0

    def update(self):
        self.get_user_input()
        self.constrain_movement()
