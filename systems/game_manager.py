from models.player import Player
from models.dungeon import Dungeon
from systems.combat_system import CombatSystem
from database.db_manager import DatabaseManager

# GameManager class to handle overall game state, player actions, and interactions 
# with the dungeon and combat system
class GameManager:
    def __init__(self, player_name):
        self.player = Player(player_name)
        self.dungeon = Dungeon()
        self.db = DatabaseManager()
        self.current_room = self.dungeon.get_room(self.player.x, self.player.y)
        self.current_room.visited = True
        self.current_enemy = None
        self.game_over = False
        self.victory = False

    # Move the player in the specified direction and handle room interactions
    def move_player(self, dx, dy):
        new_x = self.player.x + dx
        new_y = self.player.y + dy

        if 0 <= new_x < self.dungeon.width and 0 <= new_y < self.dungeon.height:
            self.player.x = new_x
            self.player.y = new_y
            self.current_room = self.dungeon.get_room(new_x, new_y)
            self.current_room.visited = True

            if self.current_room.room_type == "enemy" and self.current_room.enemy is not None:
                self.current_enemy = self.current_room.enemy
                return f"You entered a hostile room! {self.current_enemy.name} appears."

            elif self.current_room.room_type == "treasure":
                if not self.current_room.cleared:
                    self.player.gold += 20
                    self.current_room.cleared = True
                    return "You found 20 gold in a loot cache."
                return "This loot cache has already been emptied."

            elif self.current_room.room_type == "rest":
                if not self.current_room.cleared:
                    self.player.heal(15)
                    self.current_room.cleared = True
                    return "You take a moment to recover 15 HP."
                return "This recovery spot has already been used."

            return self.current_room.describe()

        return "You cannot move that way."

    # Start combat if the current room has an enemy
    def start_combat(self):
        if self.current_enemy is not None:
            return CombatSystem(self.player, self.current_enemy)
        return None

    # Handle a combat turn based on the player's chosen action and the enemy's response
    def handle_combat_turn(self, player_action):
        if self.current_enemy is None:
            return "There is no enemy to fight.", False

        combat = CombatSystem(self.player, self.current_enemy)
        log, enemy_action = combat.resolve_turn(player_action)

        if not self.current_enemy.is_alive():
            self.player.gold += self.current_enemy.gold_reward
            log += f"\nYou defeated {self.current_enemy.name} and gained {self.current_enemy.gold_reward} gold."
            self.current_room.room_type = "empty"
            self.current_room.enemy = None
            self.current_enemy = None
            return log, True

        if not self.player.is_alive():
            self.game_over = True
            log += "\nYou were defeated."
            return log, True

        return log, False

    # Use a potion to restore health if available
    def use_potion(self):
        if self.player.use_potion():
            return f"You used a potion and restored health. Current HP: {self.player.hp}"
        return "You have no potions left."

    # Save the current game state to the database
    def save_game(self):
        self.db.save_player(self.player)
        return "Game saved successfully."

    # Load the game state from the database and update the player and current room accordingly
    def load_game(self):
        row = self.db.load_player()

        if row:
            name, hp, max_hp, attack, defense, gold, potions, pos_x, pos_y = row

            self.player = Player(name)
            self.player.hp = hp
            self.player.max_hp = max_hp
            self.player.attack = attack
            self.player.defense = defense
            self.player.gold = gold
            self.player.potions = potions
            self.player.x = pos_x
            self.player.y = pos_y

            self.current_room = self.dungeon.get_room(self.player.x, self.player.y)
            self.current_enemy = None
            self.game_over = False

            return "Game loaded successfully."

        return "No saved game found."