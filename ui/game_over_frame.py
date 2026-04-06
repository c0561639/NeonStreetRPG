import customtkinter as ctk

# GameOverFrame: Displays the game over screen with results and options to return to menu or exit
class GameOverFrame(ctk.CTkFrame):
    def __init__(self, master, result_text="Game Over"):
        super().__init__(master)

        self.master = master
        self.game_manager = master.game_manager

        # Display game over title, result text, player summary, and options to return to menu or exit
        title_label = ctk.CTkLabel(
            self,
            text="Game Over",
            font=("Arial", 32, "bold")
        )
        title_label.pack(pady=(60, 20))

        result_label = ctk.CTkLabel(
            self,
            text=result_text,
            font=("Arial", 18),
            wraplength=700
        )
        result_label.pack(pady=10)

        # Display player summary if game manager is available, otherwise show no data message
        if self.game_manager is not None:
            summary_text = (
                f"Player: {self.game_manager.player.name}\n"
                f"Gold Collected: {self.game_manager.player.gold}\n"
                f"Final Position: ({self.game_manager.player.x}, {self.game_manager.player.y})"
            )
        else:
            summary_text = "No game data available."

        summary_label = ctk.CTkLabel(
            self,
            text=summary_text,
            font=("Arial", 16)
        )
        summary_label.pack(pady=20)

        # Buttons to return to main menu or exit game
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=20)

        menu_button = ctk.CTkButton(
            button_frame,
            text="Return to Main Menu",
            width=200,
            command=self.return_to_menu
        )
        menu_button.grid(row=0, column=0, padx=10, pady=10)

        exit_button = ctk.CTkButton(
            button_frame,
            text="Exit Game",
            width=200,
            command=self.master.destroy
        )
        exit_button.grid(row=0, column=1, padx=10, pady=10)

    # Handle returning to main menu by resetting game manager and showing main menu frame
    def return_to_menu(self):
        self.master.game_manager = None
        self.master.show_main_menu()