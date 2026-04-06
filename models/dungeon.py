import random
from models.room import Room
from models.enemy import Enemy

# Dungeon class to represent the game world, consisting of a grid of rooms
class Dungeon:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        self.grid = self.generate_dungeon()

    # Method to generate a random dungeon layout, populating the grid with different types of rooms
    def generate_dungeon(self):
        grid = []

        for y in range(self.height):
            row = []

            for x in range(self.width):
                room_roll = random.randint(1, 100)

                if x == 0 and y == 0:
                    row.append(Room("empty"))
                elif room_roll <= 35:
                    row.append(Room("enemy", enemy=Enemy.create_random_enemy()))
                elif room_roll <= 50:
                    row.append(Room("treasure"))
                elif room_roll <= 65:
                    row.append(Room("rest"))
                else:
                    row.append(Room("empty"))

            grid.append(row)

        return grid

    # Method to retrieve the room at a specific (x, y) coordinate in the dungeon grid
    def get_room(self, x, y):
        return self.grid[y][x]
    
    # Method to generate a string representation of the dungeon map for mapping purposes, 
    # showing the player's position and room types
    def get_debug_map_string(self, player_x=None, player_y=None):
        lines = []

        for y in range(self.height):
            row_symbols = []
            for x in range(self.width):
                if x == player_x and y == player_y:
                    row_symbols.append("*")
                elif x == 0 and y == 0:
                    row_symbols.append("S")
                else:
                    room = self.get_room(x, y)

                    symbols = {
                        "enemy": "E",
                        "treasure": "T",
                        "rest": "R",
                        "empty": "."
                    }

                    row_symbols.append(symbols.get(room.room_type, "?"))

            lines.append(" ".join(row_symbols))

        return "\n".join(lines)

    # Method to get the symbol representing the room type at a specific (x, y) coordinate, used for mapping
    def get_room_symbol(self, x, y):
        if x == 0 and y == 0:
            return "S"

        room = self.get_room(x, y)

        symbols = {
            "enemy": "E",
            "treasure": "T",
            "rest": "R",
            "empty": "."
        }

        return symbols.get(room.room_type, "?")