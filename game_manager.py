import os
import sys
import pickle # for saving and loading
import pygame

from game import Game

from holiday_type import HolidayType
from singleton_exception import SingletonException
from hero import Hero
from holiday_factory import HolidayFactory
from factory_selector import FactorySelector

from laser import Laser
from obstacle import Obstacle

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50
SPLASH_DELAY = 2000

GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

class GameManager:
    __instance = None  # Class variable for Singleton instance

    #Uses a directive and is a simpler implementation of a singleton, must be used still in conjuntion with __init__()
    # but does not use the __new__() modification process below.
    @staticmethod
    def getInstance():
        if GameManager.__instance is None:
            GameManager()
        return GameManager.__instance


    #Initilize the game manager
    def __init__(self):
        if GameManager.__instance != None:
            print("GameManager init called")
            raise SingletonException(
                "This class is a singleton!" )
        else:
            GameManager.__instance = self
            #move self.setup() he # Pygame initialization
            pygame.init()
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
            #set the title at the top of the window
            pygame.display.set_caption("Holiday Invaders")
            # Show the splash screen
            self.show_splash_screen()
            pygame.time.delay(SPLASH_DELAY)

            # Clock to control frame rate
            self.clock = pygame.time.Clock()
            #TODO:  allow for selection of holiday or random select
            self.current_holiday_type = HolidayType.HALLOWEEN
            self.current_holiday_factory = FactorySelector.get_factory(self.current_holiday_type)
            print(f"Created Factory: {self.current_holiday_factory}")
            self.game = Game(SCREEN_WIDTH, SCREEN_HEIGHT,self.current_holiday_factory)
            self.running = True

            # Game variables
            # Use a factory here
            # made assumptions on game variables, used to save and load for Memento
            # move these below to game.py?
            self.level = 1
            self.score = 0
            self.enemy_positions = []

            self.running = True

            print("Game Manager Initialized")

    def show_splash_screen(self):
        # Construct the file path for the image
        image_path = os.path.join('resources', 'holiday_invaders.png')
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(splash_image, self.screen.get_size())  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # 60 FPS limit

    def handle_events(self):
        """Handle game events like keypresses and window closing."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            # Handle other key events if necessary
            # adding save and load command
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: # save game clicking 'S'
                    self.save_game()
                elif event.type == pygame.K_l: # load game clicking 'L'
                    self.load_game()

    def update(self):
        """Update game objects."""
        self.game.hero_group.update()

    def render(self):
        """Update game objects."""
        self.screen.fill(GREY)
        # Draw the hero shooter on the bottom
        self.game.hero_group.draw(self.screen)
        # Draw all the lasers of the hero
        self.game.hero_group.sprite.lasers_group.draw(self.screen)
        #self.hero_group.sprite.laser_group.draw(self.screen)
        for obstacle in self.game.obstacles:
            obstacle.blocks_group.draw(self.screen)
        self.game.enemies_group.draw(self.screen)

        pygame.display.update()

    def stop(self):
        """Stop the game loop."""
        self.running = False

    def create_memento(self):
        # creating memento object to save current state
        return Memento(self.level, self.score, self.enemy_positions)

    def restore_memento(self):
        # restores the game from memento object
        self.level = memento.level
        self.score = memento.score
        self.enemy_positions = memento.enemy_positions

    def save_game(self, file_path="savegame.dat"):
        # saving game in binary file which library pickle uses
        memento = self.create_memento()
        with open(file_path, 'wb') as file:
            pickle.dump(memento, file)
            print("Game saved!")

    def load_game(self, file_path="savegame.dat"):
        # load the game state from a file
        if not os.path.exists(file_path):
            print("No save file found.")
            return
        with open(file_path, 'rb') as file:
            memento = pickle.load(file)
        self.restore_memento(memento)
        print("Game loaded!")


