import os
import sys
import pickle # library for saving and loading
import pygame

from game import Game
from game_data import GameData

from halloween_factory import HalloweenFactory
from holiday_type import HolidayType
from singleton_exception import SingletonException
from hero import Hero
from holiday_factory import HolidayFactory
from factory_selector import FactorySelector
from memento import Memento

from laser import Laser
from obstacle import Obstacle

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50
SPLASH_DELAY = 2000

GREY = (29, 29, 27) #background
YELLOW = (243, 216, 63) #frame

class GameManager:
    __instance = None  # Class variable for Singleton instance

    # Uses a directive and is a simpler implementation of a singleton, must be used still in conjuntion with __init__()
    # but does not use the __new__() modification process below.
    @staticmethod
    def getInstance():
        if GameManager.__instance is None:
            GameManager()
        return GameManager.__instance

    # Initilize the game manager
    def __init__(self):
        if GameManager.__instance != None:
            print("GameManager init called")
            raise SingletonException(
                "This class is a singleton!" )
        else:
            GameManager.__instance = self
            # move self.setup() he # Pygame initialization
            pygame.init()
            pygame.mixer.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
            # set the title at the top of the window
            pygame.display.set_caption("Holiday Invaders")
            # Show the splash screen
            self.show_splash_screen()
            pygame.time.delay(SPLASH_DELAY)

            # Clock to control frame rate
            self.clock = pygame.time.Clock()

            # TODO:  allow for selection of holiday or random select
            self.current_holiday_type = HolidayType.HALLOWEEN
            # self.current_holiday_type = HolidayType.THANKSGIVING
            self.current_holiday_factory = FactorySelector.get_factory(self.current_holiday_type)
            print(f"Created Factory: {self.current_holiday_factory}")
            self.game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET, self.current_holiday_factory)

            # TODO: add a play button

            self.font = pygame.font.SysFont('consolas', 40)
            # self.font = pygame.font.Font("Font/monospace.ttf", 40)
            self.level_string = f"LEVEL {self.game.get_level():02}"  # Creating the string using an f-string
            self.level_surface = self.font.render(self.level_string, False, self.current_holiday_factory.get_color())

            # Game variables
            # Use a factory here
            # made assumptions on game variables, used to save and load for Memento
            # move these below to game.py?
            self.level = 1
            self.score = 0
            self.hero_lives = 3
            self.enemy_positions = []
            self.game_running = True
            # TODO:  coalesce with game.running
            self.paused = False
            self.enemy_positions = []
            # TODO:  coalesce with game.running
            self.running = True

            # init the sounds needed for winning and losing
            sound_path = os.path.join("resources", "victory-sound.wav")
            self.victory_sound = pygame.mixer.Sound(sound_path)
            sound_path = os.path.join("resources", "game-over-sound.wav")
            self.game_over_sound = pygame.mixer.Sound(sound_path)

            print("Game Manager Initialized")

    def show_splash_screen(self):
        # Construct the file path for the image
        image_path = os.path.join('resources', 'holiday_invaders.png')
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(splash_image, self.screen.get_size())  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        pygame.display.flip()

    def show_game_over_screen(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "game-over.png")
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(
            splash_image, self.screen.get_size()
        )  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        pygame.display.flip()

    def show_halloween_background(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "halloween-background.png")
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(
            splash_image, self.screen.get_size()
        )  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        pygame.display.flip()

    def show_thanksgiving_background(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "thanksgiving-background.png")
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(
            splash_image, self.screen.get_size()
        )  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        pygame.display.flip()

    def show_christmas_background(self):
        # Construct the file path for the image
        image_path = os.path.join("resources", "christmas-background.png")
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(
            splash_image, self.screen.get_size()
        )  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while True: #self.game.running:
            self.handle_events()
            # TODO: undertand distinction between game.running and game.paused
            if not self.paused:
               self.update()

            self.render()
            self.clock.tick(60)  # 60 FPS limit
            #if self.game.running == False:
            #    # end the timers
            #    self.game_over_sound.play(0)
            #    self.show_game_over_screen()
            #    pygame.time.delay(SPLASH_DELAY)
            #    print("Present game over screen")

    def handle_events(self):
        """Handle game events like keypresses and window closing."""
        for event in pygame.event.get():
            if event.type == self.game.enemy_laser_event and self.game.running:
                self.game.shoot_enemy_laser()
            if event.type == pygame.QUIT:
                self.game.running = False
                pygame.quit()
                sys.exit()
            # Handle other key events if necessary
            # adding save and load command
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: # save game clicking 'S'
                    self.save_game()
                    self.paused = True
                if event.key == pygame.K_l: # load game clicking 'L'
                    self.load_game()
                    self.paused = False
            if event.type == pygame.KEYDOWN:
                # TODO:  This may need a game_over flag in addition to or in place of running to prevent an issue
                if event.key == pygame.K_SPACE and self.game.running == False:
                    #start the game over from a reset state
                    self.game.reset()

    def update(self):
        if self.game.running:
            """Update game objects."""
            self.game.update()
        #else:
            #self.game_over_sound.play(0)
            #self.show_game_over_screen()
            #pygame.time.delay(SPLASH_DELAY)

    def render(self):
        # TODO add in the background for each holiday level
        # set background to grey
        self.screen.fill(GREY)
        # draw a round rect border around the window with the color of the holiday_factory
        pygame.draw.rect(self.screen,
                         self.current_holiday_factory.get_color(),
                         (10,10,780,780),
                         2,
                         0,
                         60,
                         60,
                         60,
                         60)
        # draw a line at the bottom of the window to separate the lives remaining
        pygame.draw.line(self.screen,
                         self.current_holiday_factory.get_color(),
                         (25,730),
                         (775, 730),
                         3)
        # Put the current level in the bottom right hand corner
        self.screen.blit(self.level_surface, (570,740,50,50))

        remaining_lives_x = 50 # move to the right 50 pixels
        for life in range(self.game.get_lives()):
            self.screen.blit(self.game.hero_group.sprite.image, (remaining_lives_x, 745))
            remaining_lives_x += 75


        """Update game objects."""
        self.game.render(self.screen)

        pygame.display.update()

    def stop(self):
        """Stop the game loop."""
        self.running = False

    def create_memento(self):
        # creating memento object to save current state
        return Memento(self.level, self.score, self.enemy_positions, self.hero_lives)

    def restore_memento(self):
        # restores the game from memento object
        self.level = memento.level
        self.score = memento.score
        self.enemy_positions = memento.enemy_positions
        self.hero_lives = memento.hero_lives
        print(f"Game restored from Memento: {memento}")

    def save_game(self):
        memento = self.create_memento()  # Create Memento from the current game state
        self.saved_memento = memento    # Store it in the GameManager
        print("Game saved!")

    def load_game(self):
        if self.saved_memento:  # Assuming saved_memento holds the Memento object
           memento = self.saved_memento  # Get the saved state
           self.level = memento.level
           self.score = memento.score
           self.enemy_positions = memento.enemy_positions
           self.hero_lives = memento.hero_lives

           print("Game loaded!")
        else:
           print("No saved game found.")
