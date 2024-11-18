from abc import ABC, abstractmethod
from enemies.enemy import Enemy

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
    def create_hero(self, x, y) -> Enemy:
        pass

    def get_color(self):
        pass

    def print_info(self):
        pass

#TODO:  Need hero
#TODO:  Need laser color
#TODO:  Backgrounds
#TODO:  Score and font color