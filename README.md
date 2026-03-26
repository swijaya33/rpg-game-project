# Python RPG Game

A simple 2D RPG game built with Python and Pygame. This project demonstrates core game development concepts including character movement, map systems, combat, inventory, and quests.

## Features Implemented

- **Map System**: Tile-based grid system with CSV map loading
- **Character Movement**: Player character with WASD/arrow key controls
- **Combat System**: Turn-based combat with enemies
- **Inventory System**: Player inventory with items
- **Quest System**: Basic quest tracking
- **UI Elements**: Health bar, mana bar, inventory panel
- **Sound System**: Basic sound effects
- **Particle Effects**: Visual effects for combat
- **Save/Load**: Game state saving and loading
- **Game States**: Menu, playing, pause, and game over states

## Project Structure

```
rpg-game-project/
├── main.py              # Main game loop and entry point
├── game.py              # Game logic and state management
├── player.py            # Player character class
├── map.py               # Map system and tile handling
├── sound_manager.py     # Audio system
├── particle.py          # Particle effects system
├── enemy.py             # Enemy class
├── maps/                # Map files
│   └── test_map.csv     # Sample map
├── sounds/              # Sound files (placeholder)
└── requirements.txt     # Python dependencies
```

## How to Run

1. Create a virtual environment:
   ```bash
   python3 -m venv rpg_env
   source rpg_env/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install pygame
   ```

3. Run the game:
   ```bash
   python main.py
   ```

## Controls

- **WASD** or **Arrow Keys**: Move character
- **P**: Pause/Resume game
- **SPACE**: Start game (from menu)
- **R**: Restart game (after game over)
- **S**: Save game
- **L**: Load game
- **ESC**: Quit game

## Game Elements

### Player
- Health and mana stats
- Experience and leveling system
- Inventory management
- Combat abilities

### Enemies
- Different enemy types (goblins, orcs, skeletons)
- AI that follows the player
- Health bars and combat mechanics

### Map
- Tile-based environment
- Collision detection
- Different terrain types

### Quests
- Simple quest system
- Quest tracking and completion

## Future Enhancements

- Multiplayer support
- More sophisticated graphics
- Advanced quest progression tracking
- Achievement system
- Difficulty levels
- World events and dynamic content
- More complex combat mechanics
- Sound effects and background music implementation

## Dependencies

- Python 3.6+
- Pygame 2.0+

## License

This project is created for educational purposes and demonstrates core game development concepts.