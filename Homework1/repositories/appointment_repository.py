import sqlite3
from utils.db import get_db_connection

class AppointmentRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()
        conn.close()
        return [dict(appointment) for appointment in appointments]

    def get_by_id(self, appointment_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments WHERE id = ?', (appointment_id,))
        appointment = cursor.fetchone()
        conn.close()
        return dict(appointment) if appointment else None

    def create(self, appointment_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, purpose)
            VALUES (?, ?, ?, ?)
        ''', (appointment_data['patient_id'], appointment_data['doctor_id'],
              appointment_data['appointment_date'], appointment_data['purpose']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, appointment_id, appointment_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE appointments
            SET patient_id = ?, doctor_id = ?, appointment_date = ?, purpose = ?
            WHERE id = ?
        ''', (appointment_data['patient_id'], appointment_data['doctor_id'],
              appointment_data['appointment_date'], appointment_data['purpose'], appointment_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0

    def delete(self, appointment_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0