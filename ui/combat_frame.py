import os
import customtkinter as ctk
from PIL import Image
from utils.resource_path import resource_path

# CombatFrame: Handles combat encounters with enemies
class CombatFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.game_manager = master.game_manager
        self.enemy = self.game_manager.current_enemy
        self.enemy_image = self.load_enemy_image()

        title_label = ctk.CTkLabel(
            self,
            text="Combat Encounter",
            font=("Arial", 28, "bold")
        )
        title_label.pack(pady=(20, 10))

        # Player stats
        self.player_stats_label = ctk.CTkLabel(
            self,
            text=self.get_player_stats(),
            font=("Arial", 16)
        )
        self.player_stats_label.pack(pady=10)

        # Enemy image and stats
        self.enemy_image_label = ctk.CTkLabel(
            self,
            text="",
            image=self.enemy_image
        )
        self.enemy_image_label.pack(pady=10)

        self.enemy_stats_label = ctk.CTkLabel(
            self,
            text=self.get_enemy_stats(),
            font=("Arial", 16)
        )
        self.enemy_stats_label.pack(pady=10)

        # Combat log
        self.log_label = ctk.CTkLabel(
            self,
            text=f"A wild {self.enemy.name} appears!",
            font=("Arial", 16),
            wraplength=700,
            justify="left"
        )
        self.log_label.pack(pady=20)

        # Action buttons
        action_frame = ctk.CTkFrame(self)
        action_frame.pack(pady=20)

        attack_button = ctk.CTkButton(
            action_frame,
            text="Attack",
            width=120,
            command=lambda: self.handle_action("attack")
        )
        attack_button.grid(row=0, column=0, padx=10, pady=10)

        block_button = ctk.CTkButton(
            action_frame,
            text="Block",
            width=120,
            command=lambda: self.handle_action("block")
        )
        block_button.grid(row=0, column=1, padx=10, pady=10)

        rest_button = ctk.CTkButton(
            action_frame,
            text="Rest",
            width=120,
            command=lambda: self.handle_action("rest")
        )
        rest_button.grid(row=0, column=2, padx=10, pady=10)

        potion_button = ctk.CTkButton(
            action_frame,
            text="Use Potion",
            width=120,
            command=self.use_potion
        )
        potion_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Load enemy image if available
    def load_enemy_image(self):
        if self.enemy is None or not hasattr(self.enemy, "image_path"):
            return None

        if not os.path.exists(self.enemy.image_path):
            return None

        image = Image.open(resource_path(self.enemy.image_path))
        return ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(220, 220)
        )

    # Get player stats for display
    def get_player_stats(self):
        player = self.game_manager.player
        return (
            f"{player.name}  |  HP: {player.hp}/{player.max_hp}  |  "
            f"Gold: {player.gold}  |  Potions: {player.potions}"
        )

    # Get enemy stats for display
    def get_enemy_stats(self):
        if self.enemy is None:
            return "No enemy"
        return f"{self.enemy.name}  |  HP: {self.enemy.hp}/{self.enemy.max_hp}"

    # Handle player action and update combat state
    def handle_action(self, action):
        log, combat_over = self.game_manager.handle_combat_turn(action)

        self.enemy = self.game_manager.current_enemy

        self.player_stats_label.configure(text=self.get_player_stats())
        self.enemy_stats_label.configure(text=self.get_enemy_stats())
        self.log_label.configure(text=log)

        if self.enemy is not None:
            self.enemy_image = self.load_enemy_image()
            self.enemy_image_label.configure(image=self.enemy_image)

        if self.game_manager.game_over:
            self.master.show_game_over("You were defeated in combat.")
        elif combat_over:
            self.master.show_dungeon()

    # Handle using a potion and update player stats
    def use_potion(self):
        result = self.game_manager.use_potion()
        self.player_stats_label.configure(text=self.get_player_stats())
        self.log_label.configure(text=result)