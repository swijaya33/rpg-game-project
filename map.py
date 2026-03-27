import pygame
import csv
from pygame.locals import *

class Map:
    def __init__(self, map_file):
        self.map_file = map_file
        self.tile_width = 32
        self.tile_height = 32
        self.tiles = []
        self.load_map()
        
        # Calculate map dimensions
        self.width = len(self.tiles[0]) * self.tile_width if self.tiles else 0
        self.height = len(self.tiles) * self.tile_height if self.tiles else 0
    
    def load_map(self):
        try:
            with open(self.map_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.tiles.append(row)
        except FileNotFoundError:
            # Create a default map if file doesn't exist
            self.create_default_map()
    
    def create_default_map(self):
        # Create a simple 20x20 map with grass (0) and water (1) tiles
        self.tiles = []
        for y in range(20):
            row = []
            for x in range(20):
                # Create a border of water tiles
                if x == 0 or y == 0 or x == 19 or y == 19:
                    row.append('1')  # Water
                else:
                    row.append('0')  # Grass
            self.tiles.append(row)
        
        # Save the default map
        self.save_map()
    
    def save_map(self):
        with open(self.map_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.tiles)
    
    def is_walkable(self, x, y, width, height):
        # Check if position is within map bounds
        if x < 0 or y < 0:
            return False
        
        # Get tile coordinates
        tile_x = int(x / self.tile_width)
        tile_y = int(y / self.tile_height)
        
        # Check if tile coordinates are within map bounds
        if tile_x >= len(self.tiles[0]) or tile_y >= len(self.tiles):
            return False
        
        # Get tile type
        tile_type = self.tiles[tile_y][tile_x]
        
        # Tile type 1 is water (non-walkable)
        return tile_type != '1'
    
    def render(self, screen, player):
        # Calculate visible area
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Calculate camera position to keep player centered
        camera_x = player.x - screen_width // 2
        camera_y = player.y - screen_height // 2
        
        # Ensure camera doesn't go outside map boundaries
        if camera_x < 0:
            camera_x = 0
        if camera_y < 0:
            camera_y = 0
        if camera_x > self.width - screen_width:
            camera_x = self.width - screen_width
        if camera_y > self.height - screen_height:
            camera_y = self.height - screen_height
        
        # Render tiles
        for y, row in enumerate(self.tiles):
            for x, tile_type in enumerate(row):
                # Calculate screen position relative to camera
                screen_x = x * self.tile_width - camera_x
                screen_y = y * self.tile_height - camera_y
                
                # Only draw if tile is within screen bounds
                if (screen_x < screen_width and screen_x + self.tile_width > 0 and
                    screen_y < screen_height and screen_y + self.tile_height > 0):
                    
                    # Draw tile based on type
                    if tile_type == '0':  # Grass
                        pygame.draw.rect(screen, (34, 139, 34), (screen_x, screen_y, self.tile_width, self.tile_height))
                    elif tile_type == '1':  # Water
                        pygame.draw.rect(screen, (0, 0, 255), (screen_x, screen_y, self.tile_width, self.tile_height))
                    elif tile_type == '2':  # Forest
                        pygame.draw.rect(screen, (0, 100, 0), (screen_x, screen_y, self.tile_width, self.tile_height))
                    elif tile_type == '3':  # Road
                        pygame.draw.rect(screen, (128, 128, 128), (screen_x, screen_y, self.tile_width, self.tile_height))
                    
                    # Draw tile border
                    pygame.draw.rect(screen, (0, 0, 0), (screen_x, screen_y, self.tile_width, self.tile_height), 1)