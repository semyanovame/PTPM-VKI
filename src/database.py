import sqlite3
class DatabaseRepository:
    def __init__(self, db_name="mydatabase.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def add(self, comment_id:int, name:str, message:str) -> bool:
        if not isinstance(comment_id, int):
            raise TypeError("comment_id должен быть int")
        if not isinstance(name, str):
            raise TypeError("name должен быть str")
        if not isinstance(message, str):
            raise TypeError("message должен быть str")
        if len(name) > 256 or len(message) > 8096:
            raise ValueError("Input values exceed maximum length. 'name' must be <= 256 characters and 'message' must be <= 8096 characters.")

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO comments (id, name, message) VALUES (?, ?, ?)", (comment_id, name, message))
        self.connection.commit()
        return True

    def get_by_id(self, comment_id:int) -> dict:
        if not isinstance(comment_id, int):
            raise TypeError("comment_id должен быть int")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM comments WHERE id=?", (comment_id,))
        row = cursor.fetchone()
        if row:
            return {"id": row[0], "name": row[1], "message": row[2]}
        else:
            return None

    def get_by_name(self, name:str) -> list:
        if not isinstance(name, str):
            raise TypeError("name должен быть str")
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM comments WHERE name=?", (name,))
        rows = cursor.fetchall()
        return [{"id": row[0], "name": row[1], "message": row[2]} for row in rows]

    def update(self, comment_id:int, message:str) -> bool:
        if not isinstance(comment_id, int):
            raise TypeError("comment_id должен быть int")
        if not isinstance(message, str):
            raise TypeError("message должен быть str")
        cursor = self.connection.cursor()
        cursor.execute("UPDATE comments SET message=? WHERE id=?", (message, comment_id))
        self.connection.commit()
        return cursor.rowcount > 0

    def delete(self, comment_id:int) -> bool:
        if not isinstance(comment_id, int):
            raise TypeError("comment_id должен быть int")
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM comments WHERE id=?", (comment_id,))
        self.connection.commit()
        return cursor.rowcount > 0