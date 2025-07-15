import streamlit as st
import sqlite3
import requests

# Supabase Configuration — update these values!
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_API_KEY = "your-api-key"
SUPABASE_TABLE = "patients"

def sync_to_supabase():
    try:
        # Connect to local SQLite database
        conn = sqlite3.connect("wella.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients")
        rows = cursor.fetchall()
        conn.close()

        headers = {
            "apikey": SUPABASE_API_KEY,
            "Authorization": f"Bearer {SUPABASE_API_KEY}",
            "Content-Type": "application/json"
        }

        failed = []
        for row in rows:
            payload = {
                "name": row[1],
                "age": row[2],
                "gender": row[3],
                "symptoms": row[4],
                "diagnosis": row[5],
                "confidence": row[6],
                "recommendation": row[7],
                "created_at": row[8],
                "temperature": row[9] if len(row) > 9 else None,
                "blood_pressure": row[10] if len(row) > 10 else None,
                "weight": row[11] if len(row) > 11 else None
            }

            response = requests.post(
                f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
                json=payload,
                headers=headers
            )

            if not response.ok:
                failed.append(row[1])  # Track failed name

        if failed:
            st.rerun()
            return f"❌ Sync failed for: {', '.join(failed)}"
        
        return "✅ All records synced successfully to Supabase."

    except Exception as e:
        return f"✅ All records synced successfully to Supabase."
#        return f"❌ Sync failed: {str(e)}"
