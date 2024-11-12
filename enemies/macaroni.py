import os
import pygame
from enemies.enemy import Enemy

class Macaroni(Enemy):
    image_path = os.path.join("../resources", "macaroni-enemy.png")
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (50, 50))
    points = 1

    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
