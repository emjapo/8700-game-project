import os
import sys
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

from caretaker import Caretaker

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
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
            self.game = Game(SCREEN_WIDTH, SCREEN_HEIGHT,self.current_holiday_factory)
            # TODO: add a play button
            # self.game.running = True

            # Game variables
            # Use a factory here
            # made assumptions on game variables, used to save and load for Memento
            # move these below to game.py?
            self.caretaker = Caretaker()
            #self.game_state = { "level": 1, "score": 0, "player_position": (0,0) }
 

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
        self.show_startup_menu()
	
        while True: #self.game.running:
            self.handle_events()
            self.update()
            self.render()
   
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.save_game()
                self.show_startup_menu()         
   
            self.clock.tick(60)  # 60 FPS limit
            if self.game.running == False:
                # end the timers
                self.game_over_sound.play(0)
                self.show_game_over_screen()
                pygame.time.delay(SPLASH_DELAY)
                print("Present game over screen")

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
                if event.key == pygame.K_l: # load game clicking 'L'
                    self.load_game()
                if event.key == pygame.K_e:
                    self.exit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.game.running == False:
                    #start the game over from a reset state
                    self.game.reset()

    def update(self):
        if self.game.running:
            """Update game objects."""
            self.game.update()

    def render(self):
        """Update game objects."""
        self.screen.fill(GREY)
        # TODO add in the background for each holiday level
        self.game.render(self.screen)

        pygame.display.update()

    def stop(self):
        """Stop the game loop."""
        self.running = False

    def save_game(self):
        memento = self.game.create_memento()  # Create Memento from the current game state
        self.caretaker.save_memento(memento)    # save file using caretaker
        print("Game saved!")

    def load_game(self):
        memento = self.caretaker.load_memento()  # restore the saved Memento
        if memento:
            print("Loading saved game state.")
            self.game.restore_from_memento(memento)  # restore the game state from Memento
            self.game.running = True
        else:
            print("No saved game state found.")

    def exit_game(self):
        print("Exiting game...")
        self.save_game()
        pygame.quit()
        sys.exit()

    def show_startup_menu(self):
        # temporary screen for start up menu
        font = pygame.font.Font(None, 40)
        new_game_text = font.render("Press N for New Game", True, (255, 255, 0))
        load_game_text = font.render("Press L to Load Game", True, (255, 255, 0))
        exit_game_text = font.render("Press E to Exit Game", True, (255, 255, 0))
        self.screen.fill((128, 128, 128))
        self.screen.blit(new_game_text, (400, 200))
        self.screen.blit(load_game_text, (400, 300))
        self.screen.blit(exit_game_text, (400, 400))
        pygame.display.flip()
	
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:  # Start New Game
                        waiting_for_input = False
                        print("Starting new game...")
                    elif event.key == pygame.K_l:  # Load Saved Game
                        waiting_for_input = False
                        self.load_game()  # Load the saved game state from file
                    elif event.key == pygame.K_e:  # Exit the game
                        waiting_for_input = False
                        self.exit_game()

