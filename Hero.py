import pygame
import os

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

