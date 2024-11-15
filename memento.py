class Memento:
    #  class to store the game state
    def __init__(self, level, score, enemy_positions):
        self.level = level
        self.score = score
        self.enemy_positions = enemy_positions

