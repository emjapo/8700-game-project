import os
import sys
import pickle # for saving and loading

import pygame


class GameManager:
    _instance = None  # Class variable for Singleton instance

    # This will make the GameManager a singleton
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    #Initilize the game manager
    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return
        self._initialized = True
        print("Initializing game manager")

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

	# made assumptions on game variables, used to save and load for Memento
	self.level = 1
	self.score = 0
	self.enemy_positions = []

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
	    
	    # adding save and load command
	    elif event.type = pygame.KEYDOWN:
		if event.key == pygame.K_s: # save game clicking 'S'
		   self.save_game()
		elif event.type == pygame.K_l: # load game clicking 'L'
		   self.load_game()

    def update(self):
        """Update game objects."""
    def render(self):
        """Update game objects."""

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


