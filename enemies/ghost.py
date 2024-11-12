import os
from enemies.enemy import Enemy

class Ghost(Enemy):
    image = os.path.join("../resources", "ghost-enemy.png")
    def __init__(self, image, points, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.image = image
        self.points = points

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.size)
