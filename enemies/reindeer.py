import os
import pygame
from enemies.enemy import Enemy

class Reindeer(Enemy):
    image_path = os.path.join("resources", "reindeer-enemy.png")
    points = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, surface):
        image = pygame.image.load(self.image_path).convert_alpha()
        image = pygame.transform.scale(image, (50, 50))
        surface.blit(image, (self.x, self.y))
        pygame.display.flip()
