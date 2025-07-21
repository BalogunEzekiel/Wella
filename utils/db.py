import sqlite3

def get_connection():
    return sqlite3.connect("wella.db")

def drop_users_table():
    conn = sqlite3.connect("wella.db")
    cur = conn.cursor()

    # ❌ Drop the users table if it exists
    cur.execute("DROP TABLE IF EXISTS users")

    conn.commit()
    conn.close()
