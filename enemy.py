import pygame
from pygame.locals import *

class Enemy:
    def __init__(self, x, y, enemy_type="goblin"):
        self.x = x
        self.y = y
        self.width = 24
        self.height = 24
        self.speed = 2
        self.health = 50
        self.max_health = 50
        self.attack = 5
        self.defense = 2
        self.type = enemy_type
        
        # Enemy color based on type
        if enemy_type == "goblin":
            self.color = (0, 200, 0)  # Green goblin
        elif enemy_type == "orc":
            self.color = (150, 0, 0)  # Red orc
        elif enemy_type == "skeleton":
            self.color = (200, 200, 200)  # Gray skeleton
        else:
            self.color = (100, 100, 100)  # Gray default
    
    def update(self, player, game_map):
        # Simple AI: move towards player
        if player.x < self.x:
            self.x -= self.speed
        elif player.x > self.x:
            self.x += self.speed
            
        if player.y < self.y:
            self.y -= self.speed
        elif player.y > self.y:
            self.y += self.speed
        
        # Keep enemy within map boundaries
        if hasattr(game_map, 'width') and hasattr(game_map, 'height'):
            self.x = max(0, min(self.x, game_map.width - self.width))
            self.y = max(0, min(self.y, game_map.height - self.height))
    
    def render(self, screen):
        # Draw enemy as a rectangle
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
        # Draw health bar
        bar_width = 30
        bar_height = 5
        bar_x = self.x
        bar_y = self.y - 10
        
        # Health bar background
        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        
        # Health fill
        health_ratio = self.health / self.max_health
        pygame.draw.rect(screen, (255, 0, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        return self.health > 0