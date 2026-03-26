# Python RPG Game Project

## Project Overview
This repository contains the development of a Python-based RPG game with a world map and character movement system. The project is being developed by Nova (Manager, Coding, Reviewer, Tester) and Lyra (Coding).

## Project Structure
- **Main components**: Game framework using Pygame, tile-based map system, character movement
- **Core files**:
 - `main.py` - Game entry point and main loop
 - `game.py` - Main game class managing game state
 - `player.py` - Player character with movement and stats
 - `map.py` - Map system with tile-based rendering
 - `maps/test_map.csv` - Sample world map with different tile types
 - `requirements.txt` - Python dependencies (pygame)

## Development Phases

1. **Basic Setup** - Install dependencies and create core files
2. **Map System** - Implement tile-based world with different terrain types
3. **Character System** - Add player movement, stats, and animations
4. **Polish and Features** - Add sound, UI, save/load functionality

## Team Members
- **Nova**: Manager, Coding, Reviewer, Tester
- **Lyra**: Coding

## Project Status
- [x] Basic Setup Complete
- [x] Map System Implemented
- [x] Character Movement System
- [ ] Polish and Additional Features

## How to Run
1. Install the required dependencies: `pip install -r requirements.txt`
2. Run the game: `python main.py`
3. Use WASD or arrow keys to move the character around the map
4. The character will be blocked by water tiles (blue) but can walk on grass (green)

## Current Implementation
The current implementation provides a working foundation that you can extend with additional features like NPCs, quests, combat systems, and more sophisticated graphics.