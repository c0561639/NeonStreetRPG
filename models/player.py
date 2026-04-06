from models.character import Character

# Player class representing the player's character and stats
class Player(Character):
    def __init__(self, name):
        super().__init__(name, max_hp=100, attack=15, defense=5)
        self.gold = 0
        self.potions = 2
        self.x = 0
        self.y = 0
        self.inventory = []

    # Method to use a potion and heal the player
    def use_potion(self):
        if self.potions > 0:
            self.heal(25)
            self.potions -= 1
            return True
        return False