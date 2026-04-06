import os
import customtkinter as ctk
from PIL import Image
from utils.resource_path import resource_path

# DungeonFrame: Main game interface showing the current room, player stats, and movement options
class DungeonFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.master = master
        self.game_manager = master.game_manager

        self.room_images = self.load_room_images()

        # Map display
        self.map_label = ctk.CTkLabel(
            self,
            text=self.game_manager.dungeon.get_debug_map_string(
                self.game_manager.player.x,
                self.game_manager.player.y
            ),
            font=("Consolas", 18),
            justify="left"
        )
        self.map_label.pack(pady=10)

        # Room image and description
        self.room_image_label = ctk.CTkLabel(self, text="")
        self.room_image_label.pack(pady=10)

        self.room_label = ctk.CTkLabel(
            self,
            text=self.game_manager.current_room.describe(),
            font=("Arial", 16),
            wraplength=700
        )
        self.room_label.pack(pady=10)

        # Log label for room events and actions
        self.log_label = ctk.CTkLabel(
            self,
            text="Explore the neon streets...",
            font=("Arial", 14),
            wraplength=700,
            justify="left"
        )
        self.log_label.pack(pady=20)

        # Player stats display
        self.stats_label = ctk.CTkLabel(
            self,
            text=self.get_stats_text(),
            font=("Arial", 16)
        )
        self.stats_label.pack(pady=10)

        # Movement buttons
        movement_frame = ctk.CTkFrame(self)
        movement_frame.pack(pady=20)

        ctk.CTkButton(
            movement_frame,
            text="Up",
            width=100,
            command=lambda: self.move_player(0, -1)
        ).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(
            movement_frame,
            text="Left",
            width=100,
            command=lambda: self.move_player(-1, 0)
        ).grid(row=1, column=0, padx=10, pady=10)

        ctk.CTkButton(
            movement_frame,
            text="Down",
            width=100,
            command=lambda: self.move_player(0, 1)
        ).grid(row=1, column=1, padx=10, pady=10)

        ctk.CTkButton(
            movement_frame,
            text="Right",
            width=100,
            command=lambda: self.move_player(1, 0)
        ).grid(row=1, column=2, padx=10, pady=10)

        action_frame = ctk.CTkFrame(self)
        action_frame.pack(pady=20)

        # Action buttons for saving, using potions, and returning to main menu
        ctk.CTkButton(
            action_frame,
            text="Save Game",
            command=self.save_game
        ).grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkButton(
            action_frame,
            text="Use Potion",
            command=self.use_potion
        ).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(
            action_frame,
            text="Main Menu",
            command=self.master.show_main_menu
        ).grid(row=0, column=2, padx=10, pady=10)

        self.update_room_display()

    # Load room images for different room types
    def load_room_images(self):
        base_path = os.path.join("assets", "images", "rooms")

        return {
            "empty": ctk.CTkImage(
                light_image=Image.open(resource_path(os.path.join(base_path, "DungeonPlaceholder1.png"))),
                dark_image=Image.open(resource_path(os.path.join(base_path, "DungeonPlaceholder1.png"))),
                size=(256, 256)
            ),
            "enemy": ctk.CTkImage(
                light_image=Image.open(resource_path(os.path.join(base_path, "EnemyDungeonPlaceholder1.png"))),
                dark_image=Image.open(resource_path(os.path.join(base_path, "EnemyDungeonPlaceholder1.png"))),
                size=(256, 256)
            ),
            "treasure": ctk.CTkImage(
                light_image=Image.open(resource_path(os.path.join(base_path, "TreasureRoom1.png"))),
                dark_image=Image.open(resource_path(os.path.join(base_path, "TreasureRoom1.png"))),
                size=(256, 256)
            ),
            "rest": ctk.CTkImage(
                light_image=Image.open(resource_path(os.path.join(base_path, "RestRoom1.png"))),
                dark_image=Image.open(resource_path(os.path.join(base_path, "RestRoom1.png"))),
                size=(256, 256)
            ),
        }

    # Get formatted player stats for display
    def get_stats_text(self):
        player = self.game_manager.player
        return (
            f"Name: {player.name}    "
            f"HP: {player.hp}/{player.max_hp}    "
            f"Gold: {player.gold}    "
            f"Potions: {player.potions}    "
            f"Position: ({player.x}, {player.y})"
        )

    # Update the room display based on the current room type and player stats
    def update_room_display(self):
        room = self.game_manager.current_room
        room_type = room.room_type

        image = self.room_images.get(room_type, self.room_images["empty"])
        self.room_image_label.configure(image=image)

        self.room_label.configure(text=room.describe())
        self.stats_label.configure(text=self.get_stats_text())

    # Handle player movement and check for combat encounters
    def move_player(self, dx, dy):
        result = self.game_manager.move_player(dx, dy)

        self.log_label.configure(text=result)
        self.update_room_display()

        self.map_label.configure(
            text=self.game_manager.dungeon.get_debug_map_string(
                self.game_manager.player.x,
                self.game_manager.player.y))

        if self.game_manager.current_enemy is not None:
            self.master.show_combat()

    # Handle saving the game and display result in log
    def save_game(self):
        result = self.game_manager.save_game()
        self.log_label.configure(text=result)

    # Handle using a potion and update player stats
    def use_potion(self):
        result = self.game_manager.use_potion()
        self.stats_label.configure(text=self.get_stats_text())
        self.log_label.configure(text=result)