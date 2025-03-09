import sqlite3
from utils.db import get_db_connection

class DiseaseRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM diseases')
        diseases = cursor.fetchall()
        conn.close()
        return [dict(disease) for disease in diseases]

    def get_by_id(self, disease_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM diseases WHERE id = ?', (disease_id,))
        disease = cursor.fetchone()
        conn.close()
        return dict(disease) if disease else None

    def create(self, disease_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO diseases (name, type, symptoms, severity)
            VALUES (?, ?, ?, ?)
        ''', (disease_data['name'], disease_data['type'], disease_data['symptoms'], disease_data['severity']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, disease_id, disease_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE diseases
            SET name = ?, type = ?, symptoms = ?, severity = ?
            WHERE id = ?
        ''', (disease_data['name'], disease_data['type'], disease_data['symptoms'], disease_data['severity'], disease_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0

    def delete(self, disease_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM diseases WHERE id = ?', (disease_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0