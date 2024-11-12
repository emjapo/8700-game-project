from abc import ABC, abstractmethod

# Abstract enemy class
class Enemy(ABC):
    def __init__(self, image, points, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.image = image
        self.points = points

    @abstractmethod
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
