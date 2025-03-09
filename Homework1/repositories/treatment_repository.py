import sqlite3
from utils.db import get_db_connection

class TreatmentRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM treatments')
        treatments = cursor.fetchall()
        conn.close()
        return [dict(treatment) for treatment in treatments]

    def get_by_id(self, treatment_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM treatments WHERE id = ?', (treatment_id,))
        treatment = cursor.fetchone()
        conn.close()
        return dict(treatment) if treatment else None

    def create(self, treatment_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO treatments (name, description, dosage, duration, doctor_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (treatment_data['name'], treatment_data['description'], treatment_data['dosage'],
              treatment_data['duration'], treatment_data['doctor_id']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, treatment_id, treatment_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE treatments
            SET name = ?, description = ?, dosage = ?, duration = ?, doctor_id = ?
            WHERE id = ?
        ''', (treatment_data['name'], treatment_data['description'], treatment_data['dosage'],
              treatment_data['duration'], treatment_data['doctor_id'], treatment_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0

    def delete(self, treatment_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM treatments WHERE id = ?', (treatment_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0