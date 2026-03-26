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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_p and game.game_state == "playing":
                    game.toggle_pause()
                elif event.key == pygame.K_p and game.game_state == "pause":
                    game.toggle_pause()
                elif event.key == pygame.K_SPACE and game.game_state == "menu":
                    game.start_game()
                elif event.key == pygame.K_r and game.game_state == "game_over":
                    # Reset game
                    game = Game(screen)
                elif event.key == pygame.K_s and game.game_state == "playing":
                    # Save game
                    game.save_game()
                elif event.key == pygame.K_l and game.game_state == "playing":
                    # Load game
                    game.load_game()
        
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