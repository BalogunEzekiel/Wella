import sqlite3

def column_exists(cursor, table, column):
    """
    Check if a column already exists in a given SQLite table.
    """
    cursor.execute(f"PRAGMA table_info({table})")
    columns = [info[1] for info in cursor.fetchall()]
    return column in columns

def alter_patients_table():
    """
    Adds missing columns to the 'patients' table if they don't exist already.
    """
    conn = sqlite3.connect("wella.db")
    cursor = conn.cursor()

    new_columns = {
        "temperature": "TEXT",
        "blood_pressure": "TEXT",
        "weight": "TEXT",
        "appointment_date": "TEXT"
    }

    print("🔄 Checking and applying migrations for 'patients' table...")

    for col, col_type in new_columns.items():
        if not column_exists(cursor, "patients", col):
            try:
                cursor.execute(f"ALTER TABLE patients ADD COLUMN {col} {col_type}")
                print(f"✅ Added column '{col}'")
            except Exception as e:
                print(f"❌ Failed to add column '{col}': {e}")
        else:
            print(f"✔️ Column '{col}' already exists.")

    conn.commit()
    conn.close()
    print("🏁 Migration completed successfully.")
