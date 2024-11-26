# CPSC 8700
# Fall 2024
# Robert Taylor, Emily Port, Daniel Scarnavack
# Final Project
#

import json
import os

from memento import Memento

class Caretaker:
    def __init__(self, file_path="saved_game.json"):
        self.file_path = file_path
        self.saved_memento = None

    def save_memento(self, memento):
        self.saved_memento = memento
        with open(self.file_path, 'w') as file:
            json.dump(memento.get_state(), file)
        print("Game state saved to file.")

    def load_memento(self):
        try:
            with open(self.file_path, 'r') as file:
                loaded_state = json.load(file)
                print("Game state loaded from file.")
                return Memento(loaded_state)
        except FileNotFoundError:
            print("No saved game found.")
            return None

