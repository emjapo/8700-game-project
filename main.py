# CPSC 8700
# Fall 2024
# Project
#

# This is a sample Python script.
from game_manager import GameManager
from singleton_exception import SingletonException
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    try:
        game_manager = GameManager.getInstance()
    except SingletonException as e:
        print(e.args[0])
        exit(1)
    else:
        game_manager.run()

