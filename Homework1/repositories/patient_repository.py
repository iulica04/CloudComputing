from utils.db import get_db_connection

class PatientRepository:

    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients')
        patients = cursor.fetchall()
        conn.close()
        return [dict(patient) for patient in patients]

    def get_by_id(self, patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
        patient = cursor.fetchone()
        conn.close()
        return dict(patient) if patient else None

    def create(self, patient_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO patients (first_name, last_name, ssn, date_of_birth, gender, phone, email, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (patient_data['first_name'], patient_data['last_name'], patient_data['ssn'],
              patient_data['date_of_birth'], patient_data['gender'], patient_data['phone'],
              patient_data['email'], patient_data['address']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, patient_id, patient_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE patients
            SET first_name = ?, last_name = ?, ssn = ?, date_of_birth = ?, gender = ?, phone = ?, email = ?, address = ?
            WHERE id = ?
        ''', (patient_data['first_name'], patient_data['last_name'], patient_data['ssn'],
              patient_data['date_of_birth'], patient_data['gender'], patient_data['phone'],
              patient_data['email'], patient_data['address'], patient_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0

    def delete(self, patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM patients WHERE id = ?', (patient_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0