from abc import ABC, abstractmethod

# Abstract enemy class
class Enemy(ABC):

    @abstractmethod
    def draw(self, surface):
        pass
