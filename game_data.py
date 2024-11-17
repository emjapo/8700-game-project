

#Defaults Here
DEFAULT_LIVES = 3
DEFAULT_SCORE = 0
DEFAULT_LEVEL = 0

HIGH_SCORE_FILE = "high_score.txt"

class GameData:

    def __init__(self, score=DEFAULT_SCORE, lives=DEFAULT_LIVES, level=DEFAULT_LEVEL):
        self.score = score
        self.lives = lives
        self.level = level
        self.high_score = GameData.load_high_score()
        print(f"Loaded score: {self.high_score}")


    @staticmethod
    def load_high_score(file_path=HIGH_SCORE_FILE):
        try:
            with open(file_path, 'r') as file:
                high_score = int(file.readline().strip())
                return high_score
        except (FileNotFoundError, ValueError):
            GameData.save_high_score(0)
            return 0


    @staticmethod
    def save_high_score(high_score, file_path=HIGH_SCORE_FILE):
        try:
            with open(file_path, 'w') as file:
                file.write(str(high_score))
            # Return 0 if file does not exist or contains invalid data
        except OSError as e:
            print(f"Error writing to file {file_path}: {e}")
