# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
#

from abc import ABC, abstractmethod
from enemies.enemy import Enemy
from hero import Hero

# Abstract Factory Interface
class HolidayFactory(ABC):
    
    @abstractmethod
    def create_enemy_1(x, y) -> Enemy:
        pass
    @abstractmethod
    def create_enemy_2(x, y) -> Enemy:
        pass
    @abstractmethod
    def create_enemy_3(x, y) -> Enemy:
        pass
    @abstractmethod
    def create_enemy(self, type, x, y) -> Enemy:
        pass
    @abstractmethod
    def create_hero(self, x, y, offset) -> Hero:
        pass

    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def print_info(self):
        pass

    @abstractmethod
    def get_background(self):
        pass

    @abstractmethod
    def get_sound_path(self):
        pass

#TODO:  Need hero
#TODO:  Need laser color
#TODO:  Backgrounds
#TODO:  Score and font color
