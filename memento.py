class Memento:
    def __init__(self, level, score, enemy_positions, hero_lives):
        self.level = level
        self.score = score
        self.enemy_positions = enemy_positions
        self.hero_lives = hero_lives  # Store hero's number of lives

    def __str__(self):
        return f"Level: {self.level}, Score: {self.score}, Lives: {self.hero_lives}, Enemies: {len(self.enemy_positions)}"

