import sqlite3
from utils.db import get_db_connection

class DoctorRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM doctors')
        doctors = cursor.fetchall()
        conn.close()
        return [dict(doctor) for doctor in doctors]

    def get_by_id(self, doctor_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM doctors WHERE id = ?', (doctor_id,))
        doctor = cursor.fetchone()
        conn.close()
        return dict(doctor) if doctor else None

    def create(self, doctor_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO doctors (first_name, last_name, specialization, phone, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (doctor_data['first_name'], doctor_data['last_name'], doctor_data['specialization'],
              doctor_data['phone'], doctor_data['email']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, doctor_id, doctor_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE doctors
            SET first_name = ?, last_name = ?, specialization = ?, phone = ?, email = ?
            WHERE id = ?
        ''', (doctor_data['first_name'], doctor_data['last_name'], doctor_data['specialization'],
              doctor_data['phone'], doctor_data['email'], doctor_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0

    def delete(self, doctor_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM doctors WHERE id = ?', (doctor_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0