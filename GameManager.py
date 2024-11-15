import os
import sys
import pygame

from SingletonException import SingletonException

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
            print("Creating GameManager instance")
        print("Initializing game manager")

    def setup(self):
        # Pygame initialization
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        #set the title at the top of the window
        pygame.display.set_caption("Holiday Invaders")
        # Show the splash screen
        self.show_splash_screen()

        # Clock to control frame rate
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.time.delay(3000)

        # Game variables
        # Use a factory here

    def show_splash_screen(self):
        # Construct the file path for the image
        image_path = os.path.join('resources', 'holiday_invaders.png')
        splash_image = pygame.image.load(image_path)
        splash_image = pygame.transform.scale(splash_image, self.screen.get_size())  # Optionally scale to fit screen
        self.screen.blit(splash_image, (0, 0))
        # Pause for 3 seconds (3000 milliseconds)
        pygame.display.flip()
        # Pause for 3 seconds (3000 milliseconds)


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

    def update(self):
        """Update game objects."""
    def render(self):
        """Update game objects."""

    def stop(self):
        """Stop the game loop."""
        self.running = False

