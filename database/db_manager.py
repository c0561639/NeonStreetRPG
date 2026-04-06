import sqlite3

# DatabaseManager class to handle all database operations for the game
class DatabaseManager:
    def __init__(self, db_name="game_data.db"):
        self.db_name = db_name
        self.create_tables()

    # Connect to the SQLite database
    def connect(self):
        return sqlite3.connect(self.db_name)

    # Create the necessary tables in the database if they don't already exist
    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hp INTEGER NOT NULL,
            max_hp INTEGER NOT NULL,
            attack INTEGER NOT NULL,
            defense INTEGER NOT NULL,
            gold INTEGER NOT NULL,
            potions INTEGER NOT NULL,
            pos_x INTEGER NOT NULL,
            pos_y INTEGER NOT NULL
        )
        """)

        conn.commit()
        conn.close()

    # Save the player's current state to the database, replacing any existing player data
    def save_player(self, player):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM players")

        cursor.execute("""
        INSERT INTO players (name, hp, max_hp, attack, defense, gold, potions, pos_x, pos_y)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            player.name,
            player.hp,
            player.max_hp,
            player.attack,
            player.defense,
            player.gold,
            player.potions,
            player.x,
            player.y
        ))

        conn.commit()
        conn.close()

    # Load the player's state from the database, returning the most recently saved player data
    def load_player(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("""
        SELECT name, hp, max_hp, attack, defense, gold, potions, pos_x, pos_y
        FROM players
        ORDER BY id DESC
        LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()
        return row