import pygame
from player import Player
from map import Map

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Create player
        self.player = Player(100, 100)
        
        # Create map
        self.map = Map("maps/test_map.csv")
        
        # Game state
        self.running = True
    
    def update(self):
        # Update player
        self.player.update(self.map)
        
        # Update camera to follow player
        self.update_camera()
    
    def update_camera(self):
        # Simple camera that follows the player
        # In a real game, this would be more sophisticated
        pass
    
    def render(self):
        # Clear screen
        self.screen.fill((0, 0, 0))
        
        # Render map
        self.map.render(self.screen, self.player)
        
        # Render player
        self.player.render(self.screen)
        
        # Update display
        pygame.display.flip()