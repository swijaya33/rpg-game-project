import pygame
import random

class Particle:
    def __init__(self, x, y, color, size=2, speed=2):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.speed_x = random.randint(-speed, speed)
        self.speed_y = random.randint(-speed, speed)
        self.lifetime = 30  # frames to live
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1
        
    def render(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
    
    def is_dead(self):
        return self.lifetime <= 0

class ParticleSystem:
    def __init__(self):
        self.particles = []
        
    def add_particle(self, particle):
        self.particles.append(particle)
        
    def add_explosion(self, x, y, color, count=10):
        """Create an explosion effect"""
        for _ in range(count):
            self.particles.append(Particle(x, y, color, size=3, speed=3))
    
    def add_magic_effect(self, x, y, color, count=5):
        """Create a magic effect"""
        for _ in range(count):
            self.particles.append(Particle(x, y, color, size=2, speed=2))
    
    def update(self):
        # Update all particles
        for particle in self.particles[:]:  # Copy list to avoid modification during iteration
            particle.update()
            if particle.is_dead():
                self.particles.remove(particle)
    
    def render(self, screen):
        # Render all particles
        for particle in self.particles:
            particle.render(screen)