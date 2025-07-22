import sqlite3

def get_connection():
    return sqlite3.connect("wella.db")

def init_db():
    conn = sqlite3.connect("wella.db")
    cur = conn.cursor()

    # ✅ Create users table if it doesn't already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            force_password_change INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

import sqlite3

conn = sqlite3.connect("wella.db")
cursor = conn.cursor()

# Add columns if not exist
try:
    cursor.execute("ALTER TABLE patients ADD COLUMN doctor_notes TEXT")
except sqlite3.OperationalError:
    print("Column doctor_notes already exists")

try:
    cursor.execute("ALTER TABLE patients ADD COLUMN appointment_date TEXT")
except sqlite3.OperationalError:
    print("Column appointment_date already exists")

conn.commit()
conn.close()
