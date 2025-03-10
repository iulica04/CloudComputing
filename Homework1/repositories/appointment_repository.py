import sqlite3
from datetime import datetime

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

    def get_by_patient_id(self, patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments WHERE patient_id = ? ORDER BY appointment_date DESC ', (patient_id,))
        appointments = cursor.fetchall()
        conn.close()
        return [dict(appointment) for appointment in appointments] if appointments else None

    def create(self, appointment_data):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM patients WHERE id = ?', (appointment_data['patient_id'],))
        if cursor.fetchone()[0] == 0:
            conn.close()
            return None, "Patient ID not found"

        cursor.execute('SELECT COUNT(*) FROM doctors WHERE id = ?', (appointment_data['doctor_id'],))
        if cursor.fetchone()[0] == 0:
            conn.close()
            return None, "Doctor ID not found"

        appointment_date = datetime.strptime(appointment_data['appointment_date'], "%Y-%m-%d")

        if appointment_date <= datetime.now():
            conn.close()
            return None, "Appointment date must be in the future"

        cursor.execute('''
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, purpose)
            VALUES (?, ?, ?, ?)
        ''', (appointment_data['patient_id'], appointment_data['doctor_id'],
              appointment_data['appointment_date'], appointment_data['purpose']))

        conn.commit()
        conn.close()

    def update(self, appointment_id, appointment_data):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT COUNT(*) FROM appointments WHERE id = ?', (appointment_id,))
        if cursor.fetchone()[0] == 0:
            conn.close()
            return None, "Appointment ID not found"

        cursor.execute('SELECT COUNT(*) FROM patients WHERE id = ?', (appointment_data['patient_id'],))
        if cursor.fetchone()[0] == 0:
            conn.close()
            return None, "Patient ID not found"

        cursor.execute('SELECT COUNT(*) FROM doctors WHERE id = ?', (appointment_data['doctor_id'],))
        if cursor.fetchone()[0] == 0:
            conn.close()
            return None, "Doctor ID not found"

        appointment_date = datetime.strptime(appointment_data['appointment_date'], "%Y-%m-%d")
        if appointment_date <= datetime.now():
            conn.close()
            return None, "Appointment date must be in the future"

        cursor.execute('''
            UPDATE appointments
            SET patient_id = ?, doctor_id = ?, appointment_date = ?, purpose = ?
            WHERE id = ?
        ''', (appointment_data['patient_id'], appointment_data['doctor_id'],
              appointment_data['appointment_date'], appointment_data['purpose'], appointment_id))

        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return (True, None) if rows_updated > 0 else (False, "Update failed")

    def delete(self, appointment_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM appointments WHERE id = ?', (appointment_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0