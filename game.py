import pygame
from player import Player
from map import Map
from sound_manager import SoundManager
from particle import ParticleSystem
from enemy import Enemy

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        
        # Create player
        self.player = Player(100, 100)
        
        # Create map
        self.map = Map("maps/test_map.csv")
        
        # Sound manager
        self.sound_manager = SoundManager()
        
        # Particle system
        self.particle_system = ParticleSystem()
        
        # Game state
        self.running = True
        self.game_state = "menu"  # playing, menu, pause, game_over
        
        # Font for UI
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Inventory
        self.inventory = ["Health Potion", "Iron Sword", "Leather Armor"]
        
        # Quest system
        self.quests = []
        self.active_quest = None
        
        # Enemies
        self.enemies = []
        self.spawn_enemy(300, 300, "goblin")
        self.spawn_enemy(400, 400, "orc")
        self.spawn_enemy(500, 500, "skeleton")
        
        # Add a sample quest
        self.quests.append("Find the ancient sword")
        self.active_quest = self.quests[0]
        
        # Add some initial items to player inventory
        for item in self.inventory:
            self.player.add_item(item)
    
    def spawn_enemy(self, x, y, enemy_type):
        """Spawn an enemy at the specified location"""
        enemy = Enemy(x, y, enemy_type)
        self.enemies.append(enemy)
    
    def update(self):
        if self.game_state == "playing":
            # Update player
            self.player.update(self.map)
            
            # Update enemies
            for enemy in self.enemies:
                enemy.update(self.player, self.map)
            
            # Update particle system
            self.particle_system.update()
            
            # Check for collisions between player and enemies
            self.check_combat()
            
            # Update camera to follow player
            self.update_camera()
        elif self.game_state == "menu":
            # Handle menu updates if needed
            pass
        elif self.game_state == "pause":
            # Handle pause updates if needed
            pass
    
    def check_combat(self):
        """Check for combat between player and enemies"""
        for enemy in self.enemies[:]:  # Create a copy to avoid modification during iteration
            if (self.player.x < enemy.x + enemy.width and
                self.player.x + self.player.width > enemy.x and
                self.player.y < enemy.y + enemy.height and
                self.player.y + self.player.height > enemy.y):
                
                # Simple combat - player attacks enemy
                damage = self.player.attack - enemy.defense
                if damage > 0:
                    enemy.take_damage(damage)
                    self.player.add_combat_effect(self.particle_system, enemy.x, enemy.y)
                    self.sound_manager.play_sound("attack")
                
                # Enemy attacks player if still alive
                if enemy.is_alive():
                    enemy_damage = enemy.attack - self.player.defense
                    if enemy_damage > 0:
                        self.player.take_damage(enemy_damage)
                        self.sound_manager.play_sound("hit")
                
                # Remove dead enemies
                if not enemy.is_alive():
                    self.enemies.remove(enemy)
                    self.player.add_experience(25)  # Reward experience for defeating enemy
                    self.sound_manager.play_sound("enemy_defeated")
    
    def update_camera(self):
        # Simple camera that follows the player
        # In a real game, this would be more sophisticated
        pass
    
    def render(self):
        # Clear screen
        self.screen.fill((0, 0, 0))
        
        if self.game_state == "playing":
            # Render map
            self.map.render(self.screen, self.player)
            
            # Render enemies
            for enemy in self.enemies:
                enemy.render(self.screen)
            
            # Render player
            self.player.render(self.screen)
            
            # Render particles
            self.particle_system.render(self.screen)
            
            # Render UI elements
            self.render_ui()
        elif self.game_state == "menu":
            self.render_menu()
        elif self.game_state == "pause":
            self.render_pause()
        elif self.game_state == "game_over":
            self.render_game_over()
        
        # Update display
        pygame.display.flip()
    
    def render_ui(self):
        # Render health bar
        self.render_health_bar()
        
        # Render mana bar
        self.render_mana_bar()
        
        # Render inventory
        self.render_inventory()
        
        # Render quest info
        self.render_quests()
    
    def render_health_bar(self):
        # Draw health bar background
        bar_width = 200
        bar_height = 20
        bar_x = 10
        bar_y = 10
        
        pygame.draw.rect(self.screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        
        # Draw health fill
        health_ratio = self.player.health / 100.0
        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, bar_width * health_ratio, bar_height))
        
        # Draw health text
        health_text = self.small_font.render(f"Health: {self.player.health}/100", True, (255, 255, 255))
        self.screen.blit(health_text, (bar_x, bar_y - 20))
    
    def render_mana_bar(self):
        # Draw mana bar background
        bar_width = 200
        bar_height = 20
        bar_x = 10
        bar_y = 40
        
        pygame.draw.rect(self.screen, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        
        # Draw mana fill
        mana_ratio = self.player.mana / 100.0
        pygame.draw.rect(self.screen, (0, 0, 255), (bar_x, bar_y, bar_width * mana_ratio, bar_height))
        
        # Draw mana text
        mana_text = self.small_font.render(f"Mana: {self.player.mana}/100", True, (255, 255, 255))
        self.screen.blit(mana_text, (bar_x, bar_y - 20))
    
    def render_inventory(self):
        # Render inventory panel
        inventory_x = self.screen_width - 220
        inventory_y = 10
        panel_width = 200
        panel_height = 150
        
        # Draw panel background
        pygame.draw.rect(self.screen, (30, 30, 30), (inventory_x, inventory_y, panel_width, panel_height))
        pygame.draw.rect(self.screen, (100, 100, 100), (inventory_x, inventory_y, panel_width, panel_height), 2)
        
        # Draw inventory title
        title = self.small_font.render("Inventory", True, (255, 255, 255))
        self.screen.blit(title, (inventory_x + 10, inventory_y + 5))
        
        # Draw items
        for i, item in enumerate(self.inventory):
            if i < 5:  # Show only first 5 items
                item_text = self.small_font.render(f"- {item}", True, (255, 255, 255))
                self.screen.blit(item_text, (inventory_x + 10, inventory_y + 30 + i * 20))
    
    def render_quests(self):
        # Render active quest
        if self.active_quest:
            quest_text = self.small_font.render(f"Quest: {self.active_quest}", True, (255, 255, 0))
            self.screen.blit(quest_text, (10, self.screen_height - 50))
    
    def render_menu(self):
        # Render main menu
        title = self.font.render("RPG Game", True, (255, 255, 255))
        start_text = self.small_font.render("Press SPACE to Start", True, (255, 255, 255))
        
        self.screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, self.screen_height // 2 - 50))
        self.screen.blit(start_text, (self.screen_width // 2 - start_text.get_width() // 2, self.screen_height // 2))
    
    def render_pause(self):
        # Render pause screen
        pause_text = self.font.render("PAUSED", True, (255, 255, 255))
        continue_text = self.small_font.render("Press P to Continue", True, (255, 255, 255))
        
        self.screen.blit(pause_text, (self.screen_width // 2 - pause_text.get_width() // 2, self.screen_height // 2 - 50))
        self.screen.blit(continue_text, (self.screen_width // 2 - continue_text.get_width() // 2, self.screen_height // 2))
    
    def render_game_over(self):
        # Render game over screen
        game_over_text = self.font.render("GAME OVER", True, (255, 0, 0))
        restart_text = self.small_font.render("Press R to Restart", True, (255, 255, 255))
        
        self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, self.screen_height // 2 - 50))
        self.screen.blit(restart_text, (self.screen_width // 2 - restart_text.get_width() // 2, self.screen_height // 2))
    
    def toggle_pause(self):
        if self.game_state == "playing":
            self.game_state = "pause"
            self.sound_manager.play_sound("pause")
        elif self.game_state == "pause":
            self.game_state = "playing"
            self.sound_manager.play_sound("unpause")
    
    def start_game(self):
        self.game_state = "playing"
        self.sound_manager.play_sound("game_start")
    
    def game_over(self):
        self.game_state = "game_over"
        self.sound_manager.play_sound("game_over")
    
    def save_game(self, filename="savegame.json"):
        # Simple save functionality
        import json
        save_data = {
            "player_x": self.player.x,
            "player_y": self.player.y,
            "player_health": self.player.health,
            "player_mana": self.player.mana,
            "player_level": self.player.level,
            "player_experience": self.player.experience,
            "inventory": self.player.inventory,
            "quests": self.quests,
            "active_quest": self.active_quest
        }
        with open(filename, 'w') as f:
            json.dump(save_data, f)
        self.sound_manager.play_sound("save")
    
    def load_game(self, filename="savegame.json"):
        # Simple load functionality
        import json
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
                self.player.x = save_data["player_x"]
                self.player.y = save_data["player_y"]
                self.player.health = save_data["player_health"]
                self.player.mana = save_data["player_mana"]
                self.player.level = save_data["player_level"]
                self.player.experience = save_data["player_experience"]
                self.player.inventory = save_data["inventory"]
                self.quests = save_data["quests"]
                self.active_quest = save_data["active_quest"]
        except FileNotFoundError:
            pass  # No save file exists
        self.sound_manager.play_sound("load")