from abc import ABC, abstractmethod
from enemies.enemy import Enemy
from HolidayType import HolidayType

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
    def create_enemy(type, x, y) -> Enemy:
        pass
    @abstractmethod
    def create_hero( x, y) -> Enemy:
        pass
