# CPSC 8700
# Fall 2024
# Project
# Derived from https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/tree/main
#

import os
import sys
import random
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
YELLOW = (255, 255, 0)
#YELLOW = (243, 216, 63) #frame

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

            # Used for saving the game using the Memento Design Pattern
            self.caretaker = Caretaker()
            # self.game_state = { "level": 1, "score": 0, "player_position": (0,0) }


            # init the sounds needed for winning and losing
            pygame.mixer.init()
            sound_path = os.path.join("resources", "victory-sound.wav")
            self.victory_sound = pygame.mixer.Sound(sound_path)
            sound_path = os.path.join("resources", "game-over-sound.wav")
            self.game_over_sound = pygame.mixer.Sound(sound_path)
            self.holiday_sound = pygame.mixer.Sound(self.game.get_theme_sound_path())

            # Play a sound randomly
            self.holiday_sound_event = pygame.USEREVENT + 2
            # Randomly set a timer interval (between 1000ms to 5000ms)
            #self.set_holiday_sound_timer()
            timer_interval = random.randint(2000,8000)
            pygame.time.set_timer(self.holiday_sound_event, timer_interval)

    def set_holiday_sound_timer(self):
        timer_interval = random.randint(2000,8000)
        pygame.time.set_timer(self.holiday_sound_event, timer_interval)

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
            while self.game.running:
                self.handle_events()
                self.update()
                self.render()
                self.clock.tick(60)  # 60 FPS limit

            # Game Over
            self.game_over_sound.play(0)
            self.show_game_over_screen()
            # wait for the sound to finish before going to the Start Screen
            while pygame.mixer.get_busy():
                pygame.time.delay(100)

    def handle_events(self):
        """Handle game events like keypresses and window closing."""
        for event in pygame.event.get():
            if event.type == self.game.enemy_laser_event and self.game.running:
                self.game.shoot_enemy_laser()
            if event.type == pygame.QUIT:
                self.exit_game()
            # Handle other key events if necessary
            # adding save and load command
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s: # save game clicking 'S'
                    self.save_game()
                if event.key == pygame.K_l: # load game clicking 'L'
                    self.load_game()
                if event.key == pygame.K_e:
                    self.exit_game()
                if event.key == pygame.K_n:
                    self.game.next_level()
            #if event.type == pygame.KEYDOWN:
                # TODO:  This may need a game_over flag in addition to or in place of running to prevent an issue
            #    if event.key == pygame.K_SPACE and self.game.running == False:
            #        # start the game over from a reset state
            #        self.game.reset()
            # This event handles playing the Holiday sounds randomly
            if event.type == self.holiday_sound_event:
                # Play the sound in a non-blocking way
                # TODO:  Issue of overlapping sound can be resolved with a call to stop()
                #self.holiday_sound.stop()
                self.holiday_sound.play()
                # Reset the timer with a new random interval
                #self.set_holiday_sound_timer()
                timer_interval = random.randint(2000, 8000)
                pygame.time.set_timer(self.holiday_sound_event, timer_interval)
            if event.type == self.game.next_level_event:
                # stop the sound on a next level event, otherwise the sounds will bleed over
                self.holiday_sound.stop()
                # load in the new sound for the next level
                self.holiday_sound = pygame.mixer.Sound(self.game.get_theme_sound_path())
                timer_interval = random.randint(2000, 8000)
                pygame.time.set_timer(self.holiday_sound_event, timer_interval)
                #self.set_holiday_sound_timer()

    def update(self):
        if self.game.running:
            """Update game objects."""
            self.game.update()

    def render(self):
        # set background to grey
        self.screen.fill(GREY)
        self.game.render_background(self.screen)

        # render UI overlay information, score, highscore, levels and borders
        # removed in favor of background images
        #self.render_ui_borders()

        """Render game objects."""
        self.game.render_foreground(self.screen)
        """Render UI Overlays """
        self.render_level()
        self.render_score()
        self.render_highscore()
        self.render_remaining_lives()
        pygame.display.update()

    def render_remaining_lives(self):
        remaining_lives_x = 50  # move to the right 50 pixels
        for life in range(self.game.data.lives):
            self.screen.blit(self.game.hero_group.sprite.image, (remaining_lives_x, 745))
            remaining_lives_x += 75

    def render_ui_borders(self):
        # draw a round rect border around the window with the color of the holiday_factory
        pygame.draw.rect(self.screen,
                         self.game.get_theme_color()
                         (0,0,800,800),#780,780),
                         10,
                         0,
                         60,
                         60,
                         60,
                         60)
        # draw a line at the bottom of the window to separate the lives remaining
        pygame.draw.line(self.screen,
                         self.game.get_theme_color()
                         (25,730),
                         (775, 730),
                         3)
    def render_level(self):
        font = pygame.font.SysFont('consolas', 40)
        level_string = f"LEVEL {self.game.data.level:02}"  # Creating the string using an f-string
        level_surface = font.render(level_string, False, self.game.get_theme_color())
        self.screen.blit(level_surface, (570, 740, 50, 50))

    def render_score(self):
        font = pygame.font.SysFont('consolas', 40)

        score_string = str(self.game.data.score).zfill(8)  # Creating the string using an f-string
        score_surface = font.render(score_string, False, self.game.get_theme_color())
        self.screen.blit(score_surface, (50, 40, 50, 50))

        score_label_string = f"SCORE"  # Creating the string using an f-string
        score_label_surface = font.render(score_label_string, False, self.game.get_theme_color())
        self.screen.blit(score_label_surface, (50, 15, 50, 50))

    def render_highscore(self):
        font = pygame.font.SysFont('consolas', 40)

        highscore_string = str(self.game.data.high_score).zfill(8)  # Creating the string using an f-string
        highscore_surface = font.render(highscore_string, False, self.game.get_theme_color())
        self.screen.blit(highscore_surface, (540, 40, 50, 50))

        highscore_label_string = f"HIGHSCORE"  # Creating the string using an f-string
        highscore_label_surface = font.render(highscore_label_string, False,
                                              self.game.get_theme_color())
        self.screen.blit(highscore_label_surface, (540, 15, 50, 50))

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
        self.game.game_over()
        self.save_game()
        pygame.quit()
        sys.exit()

    def draw_button(self, rect, text, color):
        font = pygame.font.SysFont("consolas", 30)
        pygame.draw.rect(self.screen, color, rect)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def show_startup_menu(self):

        button_color_start = (30, 111, 80)
        button_color_load= (87, 28, 39)
        button_color_quit=(0,0,0)

        button_rect1 = pygame.Rect(
            SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 + 160, 200, 60
        )
        button_rect2 = pygame.Rect(
            SCREEN_WIDTH // 2 - 90, SCREEN_HEIGHT // 2 + 160, 200, 60
        )
        button_rect3 = pygame.Rect(
            SCREEN_WIDTH // 2 + 120 , SCREEN_HEIGHT // 2 + 160, 200, 60
        )
        mouse_pos = pygame.mouse.get_pos()
        self.draw_button(button_rect1, "Start Game", button_color_start)
        self.draw_button(button_rect2, "Load Game", button_color_load)
        self.draw_button(button_rect3, "Exit Game", button_color_quit)
        pygame.display.flip()

        # Since this screen is processed outside of the game running loop this sets up a new event handler
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.game_over()
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
                        self.game.game_over()
                        self.exit_game()
