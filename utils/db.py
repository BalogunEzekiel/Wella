import sqlite3

def get_connection():
    return sqlite3.connect("wella.db")

def init_db():
    conn = sqlite3.connect("wella.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            fullname TEXT NOT NULL,
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
