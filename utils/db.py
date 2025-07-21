import sqlite3

def get_connection():
    return sqlite3.connect("wella.db")

def init_db():
    conn = sqlite3.connect("wella.db")
    cur = conn.cursor()

    # Drop the old users table if it exists
    cur.execute("DROP TABLE IF EXISTS users")

    # Create the new users table with the force_password_change column
    cur.execute("""
        CREATE TABLE users (
            fullname TEXT NOT NULL,
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            force_password_change BOOLEAN DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()
