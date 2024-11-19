import os
import sys
import pygame

from game import Game
from game_data import GameData

from holiday_type import HolidayType
from factory_selector import FactorySelector
from singleton_exception import SingletonException
from hero import Hero
from memento import Memento

from caretaker import Caretaker

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

    # Uses a directive and is a simpler implementation of a singleton, must be used still in conjunction with __init__()
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

            self.screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
            # set the title at the top of the window
            pygame.display.set_caption("Holiday Invaders")

            # Clock to control frame rate
            self.clock = pygame.time.Clock()

            self.current_holiday_type = HolidayType.HALLOWEEN
            self.current_holiday_factory = FactorySelector.get_factory(self.current_holiday_type)
            # print(f"Created Factory: {self.current_holiday_factory}")
            self.game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
            #self.background_image = self.current_holiday_factory.get_background()
            #self.background_image = pygame.transform.scale(
            #    self.background_image, self.screen.get_size())  # Optionally scale to fit screen

            # Used for saving the game using the Memento Design Pattern
            self.caretaker = Caretaker()
            #self.game_state = { "level": 1, "score": 0, "player_position": (0,0) }
            # self.game_state = { "level": 1, "score": 0, "player_position": (0,0) }

            # TODO: move to elsewhere
            # self.running = True
            # TODO:  move to GameData
            # self.enemy_positions = []

            # init the sounds needed for winning and losing
            pygame.mixer.init()
            sound_path = os.path.join("resources", "victory-sound.wav")
            self.victory_sound = pygame.mixer.Sound(sound_path)
            sound_path = os.path.join("resources", "game-over-sound.wav")
            self.game_over_sound = pygame.mixer.Sound(sound_path)

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


    def run(self):

        self.show_splash_screen()
        pygame.time.delay(SPLASH_DELAY)
        while True:
            # Show the splash screen
            self.show_startup_menu()

            """Main game loop"""
            # while True:
            while self.game.running:
                self.handle_events()
                self.update()
                self.render()

                # TODO:  Should this move to handle_events()?
                keys = pygame.key.get_pressed()
                if keys[pygame.K_s]:
                    self.save_game()
                    self.show_startup_menu()

                self.clock.tick(60)  # 60 FPS limit
                # if self.game.running == False:
                #    # end the timers
            self.game_over_sound.play(0)
            self.show_game_over_screen()
            while pygame.mixer.get_busy():
                pygame.time.delay(100)

    def handle_events(self):
        """Handle game events like keypresses and window closing."""
        for event in pygame.event.get():
            if event.type == self.game.enemy_laser_event and self.game.running:
                self.game.shoot_enemy_laser()
            if event.type == pygame.QUIT:
                self.game.running = False
                # TODO:  Tell game that we are quitting, save high score
                self.game.game_over()
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
                # TODO:  This may need a game_over flag in addition to or in place of running to prevent an issue
                if event.key == pygame.K_SPACE and self.game.running == False:
                    # start the game over from a reset state
                    self.game.reset()

    def update(self):
        if self.game.running:
            """Update game objects."""
            self.game.update()
            # self.update_level_surface()
            # self.update_score_surface()
        # else:
        # self.game_over_sound.play(0)
        # self.show_game_over_screen()
        # pygame.time.delay(SPLASH_DELAY)

    def render(self):
        # TODO add in the background for each holiday level
        # set background to grey
        self.screen.fill(GREY)
        #self.screen.blit(self.game.background_image(), (0, 0))

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
        # self.screen.blit(self.level_surface, (570,740,50,50))
        self.screen.blit(self.render_level_surface(), (570,740,50,50))
        self.screen.blit(self.render_score_label_surface(), (50,15,50,50))
        self.screen.blit(self.render_score_surface(), (50,40,50,50))

        remaining_lives_x = 50 # move to the right 50 pixels
        for life in range(self.game.data.lives):
            self.screen.blit(self.game.hero_group.sprite.image, (remaining_lives_x, 745))
            remaining_lives_x += 75

        """Update game objects."""
        self.game.render(self.screen)

        pygame.display.update()

    def stop(self):
        """Stop the game loop."""
        self.running = False

    def render_level_surface(self):
        font = pygame.font.SysFont('consolas', 40)
        level_string = f"LEVEL {self.game.data.level:02}"  # Creating the string using an f-string
        level_surface = font.render(level_string, False, self.current_holiday_factory.get_color())
        return level_surface

    def render_score_surface(self):
        font = pygame.font.SysFont('consolas', 40)
        score_string = str(self.game.data.score).zfill(8)  # Creating the string using an f-string
        score_surface = font.render(score_string, False, self.current_holiday_factory.get_color())
        return score_surface

    def render_score_label_surface(self):
        font = pygame.font.SysFont('consolas', 40)
        score_label_string = f"SCORE"  # Creating the string using an f-string
        score_label_surface = font.render(score_label_string, False, self.current_holiday_factory.get_color())
        return score_label_surface

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

    def draw_button(self, rect, text, color):
        font = pygame.font.Font(None, 40)
        pygame.draw.rect(self.screen, color, rect)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def show_startup_menu(self):
        
        button_color_start = (30, 111, 80)
        button_color_load= (87, 28, 39)
        button_color_quit=(0,0,0)
        
        button_rect1 = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20, 200, 60
        )
        button_rect2 = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 60, 200, 60
        )
        button_rect3 = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 140, 200, 60
        )
        mouse_pos = pygame.mouse.get_pos()
        self.draw_button(button_rect1, "Start Game", button_color_start)
        self.draw_button(button_rect2, "Load Game", button_color_load)
        self.draw_button(button_rect3, "Exit Game", button_color_quit)
        pygame.display.flip()

        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect1.collidepoint(event.pos):
                        waiting_for_input = False
                        print("Starting new game...")
                        self.game.start()
                    elif button_rect2.collidepoint(event.pos):
                        waiting_for_input = False
                        self.load_game()  # Load the saved game state from file
                    elif button_rect3.collidepoint(event.pos):
                        waiting_for_input = False
                        self.exit_game()
