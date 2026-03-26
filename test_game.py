#!/usr/bin/env python3
"""
Test script to verify the RPG game components work correctly
"""

import sys
import os

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported successfully"""
    try:
        from game import Game
        from player import Player
        from map import Map
        from sound_manager import SoundManager
        from particle import ParticleSystem, Particle
        from enemy import Enemy
        
        print("✓ All modules imported successfully")
        return True
    except Exception as e:
        print(f"✗ Import test failed: {e}")
        return False

def test_player_creation():
    """Test player creation and basic functionality"""
    try:
        from player import Player
        
        player = Player(100, 100)
        assert player.x == 100
        assert player.y == 100
        assert player.health == 100
        assert player.max_health == 100
        assert player.inventory == []
        
        print("✓ Player creation and basic properties work")
        return True
    except Exception as e:
        print(f"✗ Player test failed: {e}")
        return False

def test_enemy_creation():
    """Test enemy creation and basic functionality"""
    try:
        from enemy import Enemy
        
        enemy = Enemy(200, 200, "goblin")
        assert enemy.x == 200
        assert enemy.y == 200
        assert enemy.type == "goblin"
        assert enemy.health == 50
        assert enemy.max_health == 50
        
        print("✓ Enemy creation and basic properties work")
        return True
    except Exception as e:
        print(f"✗ Enemy test failed: {e}")
        return False

def test_map_creation():
    """Test map creation"""
    try:
        from map import Map
        
        # Test with a simple map file (will create one if it doesn't exist)
        map_obj = Map("maps/test_map.csv")
        print("✓ Map creation works")
        return True
    except Exception as e:
        print(f"✗ Map test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Running RPG Game Tests...")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_player_creation,
        test_enemy_creation,
        test_map_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())