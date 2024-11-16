from abc import ABC, abstractmethod

# Abstract enemy class
# TODO:  adjust to have sprite as superclass and not ABC, maybe this will work
# TODO:  modify to follow the Alien class functions from the example
class Enemy(ABC):

    @abstractmethod
    def draw(self, surface):
        pass
