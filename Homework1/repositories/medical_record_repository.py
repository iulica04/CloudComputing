from utils.db import get_db_connection

class MedicalRecordRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medical_records')
        medical_records = cursor.fetchall()
        conn.close()
        return [dict(medical_record) for medical_record in medical_records]

    def get_by_id(self, medical_record_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medical_records WHERE id = ?', (medical_record_id,))
        medical_record = cursor.fetchone()
        conn.close()
        return dict(medical_record) if medical_record else None

    def get_by_patient_id(self, patient_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medical_records WHERE patient_id = ?', (patient_id,))
        medical_records = cursor.fetchall()
        conn.close()
        return [dict(medical_record) for medical_record in medical_records] if medical_records else None

    def get_by_disease_id(self, disease_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medical_records WHERE disease_id = ?', (disease_id,))
        medical_records = cursor.fetchall()
        conn.close()
        return [dict(medical_record) for medical_record in medical_records] if medical_records else None

    def _check_id_exists(self, table_name, id_column, id_value):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(f'SELECT 1 FROM {table_name} WHERE {id_column} = ?', (id_value,))
        result = cursor.fetchone()
        conn.close()
        return result is not None

    def create(self, medical_record_data):
        if not self._check_id_exists('patients', 'id', medical_record_data['patient_id']):
            return None, 'Patient ID not found'
        if not self._check_id_exists('diseases', 'id', medical_record_data['disease_id']):
            return None, 'Disease ID not found'
        if not self._check_id_exists('treatments', 'id', medical_record_data['treatment_id']):
            return None, 'Treatment ID not found'

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            INSERT INTO medical_records (patient_id, disease_id, treatment_id, record_date, notes) 
            VALUES (?, ?, ?, ?, ?) 
        ''', (medical_record_data['patient_id'], medical_record_data['disease_id'],
              medical_record_data['treatment_id'], medical_record_data['record_date'], medical_record_data['notes']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id, None

    def update(self, medical_record_id, medical_record_data):
        # validate the existence of patients, diseases, and treatments
        if not self._check_id_exists('patients', 'id', medical_record_data['patient_id']):
            return False, 'Patient ID not found'
        if not self._check_id_exists('diseases', 'id', medical_record_data['disease_id']):
            return False, 'Disease ID not found'
        if not self._check_id_exists('treatments', 'id', medical_record_data['treatment_id']):
            return False, 'Treatment ID not found'

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE medical_records
            SET patient_id = ?, disease_id = ?, treatment_id = ?, record_date = ?, notes = ?
            WHERE id = ?
        ''', (medical_record_data['patient_id'], medical_record_data['disease_id'],
              medical_record_data['treatment_id'], medical_record_data['record_date'],
              medical_record_data['notes'], medical_record_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0, None

    def delete(self, medical_record_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM medical_records WHERE id = ?', (medical_record_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0
