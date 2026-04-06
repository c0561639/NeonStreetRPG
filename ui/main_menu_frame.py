import customtkinter as ctk

# Main menu frame for the Neon Crawl game
class MainMenuFrame(ctk.CTkFrame):
    def __init__(self, master, message=""):
        super().__init__(master)

        self.master = master

        # Set up the main menu UI
        title_label = ctk.CTkLabel(
            self,
            text="Neon Crawl",
            font=("Arial", 32, "bold")
        )
        title_label.pack(pady=(60, 20))

        subtitle_label = ctk.CTkLabel(
            self,
            text="A Cyberpunk Dungeon Crawler",
            font=("Arial", 18)
        )
        subtitle_label.pack(pady=(0, 30))

        # Player name entry
        self.name_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter your name",
            width=250,
            height=40
        )
        self.name_entry.pack(pady=10)

        # Buttons for new game, load game, and exit
        new_game_button = ctk.CTkButton(
            self,
            text="New Game",
            width=200,
            height=40,
            command=self.start_new_game
        )
        new_game_button.pack(pady=10)

        load_game_button = ctk.CTkButton(
            self,
            text="Load Game",
            width=200,
            height=40,
            command=self.master.load_existing_game
        )
        load_game_button.pack(pady=10)

        exit_button = ctk.CTkButton(
            self,
            text="Exit",
            width=200,
            height=40,
            fg_color="darkred",
            hover_color="red",
            command=self.master.destroy
        )
        exit_button.pack(pady=10)

        # Display any messages (like errors) below the buttons
        self.message_label = ctk.CTkLabel(
            self,
            text=message,
            font=("Arial", 14)
        )
        self.message_label.pack(pady=20)

    # Method to start a new game, called when the "New Game" button is pressed
    def start_new_game(self):
        player_name = self.name_entry.get().strip()

        if not player_name:
            self.message_label.configure(text="Please enter a name.")
            return

        self.master.start_new_game(player_name)