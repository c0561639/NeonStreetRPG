# Room class representing each room in the dungeon
class Room:
    def __init__(self, room_type="empty", enemy=None, item=None):
        self.room_type = room_type
        self.enemy = enemy
        self.item = item
        self.visited = False
        self.cleared = False

    # Describe the room based on its room type
    def describe(self):
        if self.room_type == "enemy" and self.enemy is not None:
            return f"A hostile {self.enemy.name} is here!"
        elif self.room_type == "treasure":
            if self.cleared:
                return "An opened loot cache sits in the room."
            return "You found a treasure room."
        elif self.room_type == "rest":
            if self.cleared:
                return "A bedroll lays on the ground."
            return "A quiet room. You can catch your breath here."
        return "The room is empty."