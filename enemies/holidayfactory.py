from abc import ABC, abstractmethod

# Abstract Factory Interface
class HolidayFactory(ABC):
    
    @abstractmethod
    def create_enemy_1(self) -> Enemy:
        pass
    @abstractmethod
    def create_enemy_2(self) -> Enemy:
        pass
    @abstractmethod
    def create_enemy_3(self) -> Enemy:
        pass
