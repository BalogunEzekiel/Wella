import sqlite3

def get_connection():
    return sqlite3.connect("wella.db")

def init_db():
    conn = sqlite3.connect("wella.db")
    cur = conn.cursor()

    # Drop the old users table if it exists
    cur.execute("DROP TABLE IF EXISTS users")

    # Create the new users table with id and force_password_change columns
    cur.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            force_password_change BOOLEAN DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
