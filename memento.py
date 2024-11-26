# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
class Memento:
    def __init__(self, game_state):
        self.game_state = game_state

    def get_state(self):
        return self.game_state

