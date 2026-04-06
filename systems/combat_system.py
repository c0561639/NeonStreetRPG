# Rock-Paper-Scissors style combat system to handle turn-based combat between player and enemies
class CombatSystem:
    VALID_ACTIONS = ["attack", "block", "rest"]

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    # Resolve a combat turn based on player and enemy actions
    def resolve_turn(self, player_action):
        if player_action not in self.VALID_ACTIONS:
            return "Invalid action selected.", None

        enemy_action = self.enemy.choose_action()
        log = []

        log.append(f"{self.player.name} chose {player_action}.")
        log.append(f"{self.enemy.name} chose {enemy_action}.")

        # Player attacks while enemy rests
        if player_action == "attack" and enemy_action == "rest":
            damage = self.enemy.take_damage(self.player.attack + 5)
            log.append(f"Direct hit! {self.enemy.name} takes {damage} damage.")

        # Both attack
        elif player_action == "attack" and enemy_action == "attack":
            enemy_damage = self.enemy.take_damage(self.player.attack)
            player_damage = self.player.take_damage(self.enemy.attack)
            log.append(
                f"Both attacked! {self.enemy.name} takes {enemy_damage} damage "
                f"and {self.player.name} takes {player_damage} damage.")

        # Player attacks while enemy blocks
        elif player_action == "attack" and enemy_action == "block":
            damage = self.enemy.take_damage(max(1, self.player.attack // 2))
            log.append(f"{self.enemy.name} blocks! Only {damage} damage is dealt.")

        # Player blocks while enemy attacks
        elif player_action == "block" and enemy_action == "attack":
            damage = self.player.take_damage(max(1, self.enemy.attack // 2))
            log.append(f"{self.player.name} blocks and only takes {damage} damage.")

        # Player blocks while enemy rests
        elif player_action == "block" and enemy_action == "rest":
            self.enemy.heal(10)
            log.append(f"{self.enemy.name} rests and recovers 10 HP.")

        # Both block
        elif player_action == "block" and enemy_action == "block":
            log.append("Both fighters stay defensive. Nothing happens.")

        # Player rests while enemy attacks
        elif player_action == "rest" and enemy_action == "attack":
            damage = self.player.take_damage(self.enemy.attack + 5)
            log.append(f"{self.player.name} was caught resting and takes {damage} damage.")

        # Player rests while enemy blocks
        elif player_action == "rest" and enemy_action == "block":
            self.player.heal(10)
            log.append(f"{self.player.name} rests safely and recovers 10 HP.")

        # Both rest
        elif player_action == "rest" and enemy_action == "rest":
            self.player.heal(10)
            self.enemy.heal(10)
            log.append("Both fighters rest and recover 10 HP.")

        return "\n".join(log), enemy_action