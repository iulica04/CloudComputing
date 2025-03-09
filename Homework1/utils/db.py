# utils/db.py
import sqlite3
import os

def get_db_connection():
    try:
        db_path = os.path.join(os.path.dirname(__file__), '..', 'medical_system.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Eroare la conectarea la baza de date: {e}")
        raise