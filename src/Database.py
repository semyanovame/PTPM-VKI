import sqlite3
class Database:
    def __init__(self, db_name="mydatabase.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            confirm_password TEXT NOT NULL,
            result TEXT NOT NULL,
            error_message TEXT
        )
        """)
        self.connection.commit()
    def add_data(self, login, password, confirm_password, result, error_message):
        self.connection.execute("""
        INSERT INTO users (login, password, confirm_password, result, error_message)
        VALUES (?, ?, ?, ?, ?)
        """, (login, password, confirm_password, result, error_message))
        self.connection.commit()
    def get_data(self):
        cursor = self.connection.execute("SELECT * FROM users")
        data = cursor.fetchall()
        return data
    def delete_data(self, user_id):
        self.connection.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()
    def does_user_exist(self, login):
        cursor = self.connection.execute("SELECT * FROM users WHERE login = ?", (login,))
        return cursor.fetchone() is not None
    def close(self):
        self.connection.close()