# This is a sample Python script.
from GameManager import GameManager
from SingletonException import SingletonException
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
        game_manager.setup()
        game_manager.run()

