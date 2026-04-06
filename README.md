#THIS FILE WAS AI GENERATED

# Neon Streets

Neon Streets is a cyberpunk-themed dungeon crawler built in Python for a class project.  
The game combines Object-Oriented Programming, an SQLite3 database, and a CustomTkinter GUI into a playable turn-based RPG experience.

## Features

- Cyberpunk dungeon crawler setting
- Randomly generated dungeon grid
- Turn-based combat system
- Enemy encounters with unique stats
- Treasure and rest rooms
- GUI built with CustomTkinter
- Enemy and room images for "immersion"

## Technologies Used

- **Python**
- **CustomTkinter**
- **SQLite3**
- **Pillow**
- **PyInstaller** (for building the executable)

## Object-Oriented Programming Concepts Used

This project was designed around OOP principles, including:

- **Classes and Objects**
- **Inheritance**
- **Encapsulation**
- **Modular Design**

### Main Classes

- `Character` – Base class for all characters
- `Player` – Stores player stats, position, inventory, and potions
- `Enemy` – Stores enemy stats, rewards, actions, and image paths
- `Room` – Represents individual dungeon rooms
- `Dungeon` – Generates and manages the dungeon grid
- `CombatSystem` – Handles turn-based combat logic
- `GameManager` – Controls overall game logic
- `DatabaseManager` – Handles save/load functionality using SQLite

## Game Overview

The player explores a randomly generated dungeon made up of different room types:

- **Empty Rooms**
- **Enemy Rooms**
- **Treasure Rooms**
- **Rest Rooms**

When the player enters an enemy room, the game switches to a combat screen where they can choose actions such as:

- **Attack**
- **Block**
- **Rest**
- **Use Potion**

The goal is to survive encounters, collect gold, and explore the dungeon.

## Database Functionality

The game uses **SQLite3** to store save data.  
This includes:

- Player name
- HP
- Attack and defense stats
- Gold
- Potions
- Player position
- Save slot information

## GUI Functionality

The game interface is built using **CustomTkinter** and includes:

- Main menu
- Dungeon exploration screen
- Combat screen
- Game over screen

The GUI also displays:

- Room images
- Enemy images
- Player stats
- Combat logs
- Debug dungeon map for testing

Installation
1. Clone or download the project
git clone <your-repo-url>
cd Neon-Streets
2. Install dependencies
pip install customtkinter pillow
Running the Game

Run the project with:

python main.py

Or on Windows:

py main.py
Building the Executable

To compile the project into a Windows .exe file using PyInstaller:

py -m PyInstaller --onefile --windowed --name "NeonStreets" --add-data "assets;assets" main.py
Future Improvements

Possible future upgrades include:

Boss enemies
Inventory system expansion
More room/event types
Better combat animations
Player portraits
Sound effects and music
Full minimap display
Author

Sean Clarke
Computer Programming Student
Lambton College

License

This project was created for educational purposes.