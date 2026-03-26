import pygame
import sys
from game import Game

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Python RPG Game")
    
    # Create game instance
    game = Game(screen)
    
    # Main game loop
    clock = pygame.time.Clock()
    running = True
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Update game state
        game.update()
        
        # Render game
        game.render()
        
        # Cap the frame rate
        clock.tick(FPS)
    
    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()