import pygame
from pygame.locals import *
from particle import Particle

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.speed = 5
        self.health = 100
        self.mana = 100
        self.max_health = 100
        self.max_mana = 100
        self.level = 1
        self.experience = 0
        self.attack = 10
        self.defense = 5
        self.inventory = []
        
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
        health_text = font.render(f"HP: {self.health}/{self.max_health}", True, (255, 255, 255))
        mana_text = font.render(f"MP: {self.mana}/{self.max_mana}", True, (255, 255, 255))
        screen.blit(health_text, (self.x, self.y - 20))
        screen.blit(mana_text, (self.x, self.y - 40))
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health
    
    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        return False
    
    def restore_mana(self, amount):
        self.mana += amount
        if self.mana > self.max_mana:
            self.mana = self.max_mana
    
    def add_experience(self, amount):
        self.experience += amount
        # Simple level up logic
        if self.experience >= self.level * 100:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.max_mana += 10
        self.mana = self.max_mana
        self.attack += 2
        self.defense += 1
    
    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
    
    def attack_target(self, target):
        # Simple combat system
        damage = max(1, self.attack - target.defense)
        target.take_damage(damage)
        return damage
    
    def add_combat_effect(self, particle_system, x, y, color=(255, 0, 0)):
        """Add visual effect when attacking"""
        if particle_system:
            for _ in range(5):
                particle_system.add_particle(Particle(x, y, color, size=2, speed=2))