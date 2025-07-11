import sqlite3
import requests
import os

# Replace with your Supabase details
SUPABASE_URL = "https://<your-project>.supabase.co"
SUPABASE_API_KEY = "<your-api-key>"
SUPABASE_TABLE = "patients"

def sync_to_supabase():
    try:
        conn = sqlite3.connect("medguide.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients")
        rows = cursor.fetchall()
        conn.close()

        headers = {
            "apikey": SUPABASE_API_KEY,
            "Authorization": f"Bearer {SUPABASE_API_KEY}",
            "Content-Type": "application/json"
        }

        for row in rows:
            payload = {
                "name": row[1],
                "age": row[2],
                "gender": row[3],
                "symptoms": row[4],
                "diagnosis": row[5],
                "confidence": row[6],
                "recommendation": row[7],
                "created_at": row[8]
            }

            response = requests.post(
                f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
                json=payload,
                headers=headers
            )

            if not response.ok:
                return f"❌ Sync failed for record: {payload['name']}"

        return "✅ All records synced successfully to Supabase."

    except Exception as e:
        return f"❌ Sync failed: {str(e)}"
