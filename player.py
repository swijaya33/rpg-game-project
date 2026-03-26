import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.speed = 5
        self.health = 100
        self.mana = 100
        
        # Player animation
        self.animation_frame = 0
        self.animation_counter = 0
        
        # Player color (temporary)
        self.color = (255, 0, 0)  # Red player
    
    def update(self, game_map):
        # Get pressed keys
        keys = pygame.key.get_pressed()
        
        # Store old position
        old_x = self.x
        old_y = self.y
        
        # Handle movement
        if keys[K_LEFT] or keys[K_a]:
            self.x -= self.speed
        if keys[K_RIGHT] or keys[K_d]:
            self.x += self.speed
        if keys[K_UP] or keys[K_w]:
            self.y -= self.speed
        if keys[K_DOWN] or keys[K_s]:
            self.y += self.speed
        
        # Check for collisions with map boundaries
        if not game_map.is_walkable(self.x, self.y, self.width, self.height):
            # Revert to old position if collision occurs
            self.x = old_x
            self.y = old_y
        
        # Update animation
        self.animation_counter += 1
        if self.animation_counter >= 10:  # Change frame every 10 ticks
            self.animation_frame = (self.animation_frame + 1) % 4
            self.animation_counter = 0
    
    def render(self, screen):
        # Draw player as a simple rectangle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        # Draw player stats
        font = pygame.font.Font(None, 24)
        health_text = font.render(f"HP: {self.health}", True, (255, 255, 255))
        mana_text = font.render(f"MP: {self.mana}", True, (255, 255, 255))
        screen.blit(health_text, (self.x, self.y - 20))
        screen.blit(mana_text, (self.x, self.y - 40))