# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
# Derived from https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/tree/main

import os
import pygame
import random
from enemies.enemy import Enemy

SHIP_SPEED = 3

class BonusEnemy(Enemy):
    image_path = os.path.join("resources", "cake80.png")
    points = 500
    def __init__(self, screen_width):
        super().__init__()
        # randomly choose either the left or the right side of the screen, set to the x value for the initial placement
        self.screen_width = screen_width
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (50,50))
        x = random.choice([0, self.screen_width - self.image.get_width()])
        if x == 0:
            self.speed = SHIP_SPEED
        else:
            self.speed = -SHIP_SPEED
        y = 70
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        self.rect.x += self.speed
        # if the bonus enemy moves outside the window, kill() to remove from the game
        if self.rect.right > self.screen_width: # moved off the right
            self.kill()
        elif self.rect.left < 0:
            self.kill()

    def get_points(self):
        return self.points