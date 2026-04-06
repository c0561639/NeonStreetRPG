from models.character import Character
import random

# Enemy class representing each enemy type and its stats
class Enemy(Character):
    ENEMY_TYPES = [
        {
            "name": "Security Drone",
            "max_hp": 35,
            "attack": 12,
            "defense": 3,
            "gold_reward": 15,
            "image_path": "assets/images/enemies/security_drone.png"
        },
        {
            "name": "Chrome Thug",
            "max_hp": 45,
            "attack": 10,
            "defense": 2,
            "gold_reward": 12,
            "image_path": "assets/images/enemies/chrome_thug.png"
        },
        {
            "name": "Rogue Android",
            "max_hp": 40,
            "attack": 11,
            "defense": 4,
            "gold_reward": 18,
            "image_path": "assets/images/enemies/rogue_android.png"
        },
        {
            "name": "Neon Assassin",
            "max_hp": 30,
            "attack": 15,
            "defense": 2,
            "gold_reward": 20,
            "image_path": "assets/images/enemies/neon_assassin.png"
        },
        {
            "name": "Junk Hacker",
            "max_hp": 38,
            "attack": 9,
            "defense": 3,
            "gold_reward": 14,
            "image_path": "assets/images/enemies/junk_hacker.png"
        }
    ]

    def __init__(self, name, max_hp, attack, defense, gold_reward, image_path):
        super().__init__(name, max_hp, attack, defense)
        self.gold_reward = gold_reward
        self.image_path = image_path

    # Enemy AI to choose an action during combat
    def choose_action(self):
        return random.choice(["attack", "block", "rest"])

    # Factory method to create a random enemy instance
    @classmethod
    def create_random_enemy(cls):
        enemy_data = random.choice(cls.ENEMY_TYPES)
        return cls(
            enemy_data["name"],
            enemy_data["max_hp"],
            enemy_data["attack"],
            enemy_data["defense"],
            enemy_data["gold_reward"],
            enemy_data["image_path"]
        )