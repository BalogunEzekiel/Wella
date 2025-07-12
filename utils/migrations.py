import sqlite3

def alter_patients_table():
    conn = sqlite3.connect("wella.db")
    cursor = conn.cursor()

    # Add columns only if they don't already exist
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN temperature TEXT")
    except sqlite3.OperationalError:
        print("✔️ 'temperature' column already exists.")

    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN blood_pressure TEXT")
    except sqlite3.OperationalError:
        print("✔️ 'blood_pressure' column already exists.")

    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN weight TEXT")
    except sqlite3.OperationalError:
        print("✔️ 'weight' column already exists.")

    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN appointment_date TEXT")
    except sqlite3.OperationalError:
        print("✔️ 'appointment_date' column already exists.")

    conn.commit()
    conn.close()
    print("✅ Migration completed successfully.")
