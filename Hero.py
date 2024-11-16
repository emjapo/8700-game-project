import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, type, screen_width, screen_height):
        super().__init__()
        self.screen_width = -screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("resources/hero.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2,self.screen_height)) #middle and bottom

