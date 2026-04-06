
# Defines the Character class for the game
class Character:
    def __init__(self, name, max_hp, attack, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense

    # Method to apply damage to the character, taking into account their defense
    def take_damage(self, amount):
        damage = max(0, amount - self.defense)
        self.hp = max(0, self.hp - damage)
        return damage

    # Method to heal the character, ensuring that their HP does not exceed their maximum HP
    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    # Method to check if the character is still alive (HP greater than 0)
    def is_alive(self):
        return self.hp > 0