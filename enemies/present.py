# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
#

import os
import pygame
from enemies.enemy import Enemy

class Present(Enemy):
    image_path = os.path.join("resources", "present-enemy.png")
    points = 5

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        image = pygame.image.load(self.image_path).convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        surface.blit(image, (self.x, self.y))
        self.rect = image.get_rect(topleft=(self.x, self.y))
        pygame.display.flip()

    def update(self, direction):
        self.rect.x += direction
    def get_points(self):
        return self.points
