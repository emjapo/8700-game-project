# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
#

from abc import abstractmethod
import pygame

# Abstract enemy class
# TODO:  adjust to have sprite as superclass and not ABC, maybe this will work
# TODO:  modify to follow the Alien class functions from the example
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def update(self, direction):
        pass

    @abstractmethod
    def get_points(self):
        pass

