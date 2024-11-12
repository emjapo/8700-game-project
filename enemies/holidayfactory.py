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
