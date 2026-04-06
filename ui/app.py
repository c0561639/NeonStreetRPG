import customtkinter as ctk
from systems.game_manager import GameManager

# Main UI application class that manages the different frames and game states
class GameApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Neon Crawl")
        self.geometry("1000x900")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.current_frame = None
        self.game_manager = None

        self.show_main_menu()

    # Helper method to switch between different frames in the application
    def switch_frame(self, frame_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    # Start a new game by initializing the GameManager with the player's 
    # name and showing the dungeon frame
    def start_new_game(self, player_name):
        self.game_manager = GameManager(player_name)
        self.show_dungeon()

    # Load an existing game by initializing the GameManager and attempting to load 
    # the saved game state. If successful, show the dungeon frame; otherwise, 
    # return to the main menu
    def load_existing_game(self):
        self.game_manager = GameManager("Player")
        message = self.game_manager.load_game()

        if "successfully" in message.lower():
            self.show_dungeon()
        else:
            self.show_main_menu(message)

    # Show the main menu frame, optionally with a message (e.g., after loading a game)
    def show_main_menu(self, message=""):
        from ui.main_menu_frame import MainMenuFrame
        self.switch_frame(MainMenuFrame, message)

    # Show the dungeon frame
    def show_dungeon(self):
        from ui.dungeon_frame import DungeonFrame
        self.switch_frame(DungeonFrame)

    # Show the combat frame
    def show_combat(self):
        from ui.combat_frame import CombatFrame
        self.switch_frame(CombatFrame)

    # Show the game over frame
    def show_game_over(self, result_text="Game Over"):
        from ui.game_over_frame import GameOverFrame
        self.switch_frame(GameOverFrame, result_text)