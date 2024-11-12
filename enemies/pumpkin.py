import os
import pygame
from enemies.enemy import Enemy

class Pumpkin(Enemy):
    image_path = os.path.join("../resources", "pumpkin-enemy.png")
    image = pygame.image.load(image_path).convert_alpha()
    image = pygame.transform.scale(image, (50, 50))
    points = 10

    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
