from utils.db import get_db_connection
class MedicationRepository:
    def get_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medications')
        medications = cursor.fetchall()
        conn.close()
        return [dict(medication) for medication in medications]

    def get_by_id(self, medication_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medications WHERE id = ?', (medication_id,))
        medication = cursor.fetchone()
        conn.close()
        return dict(medication) if medication else None


    def get_by_disease_type(self, disease_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'SELECT name, type, dosage, ingredients, administration, adverse_effects FROM medications WHERE for_disease = ?',
            (disease_name,))
        medications = cursor.fetchall()
        conn.close()
        return [
            dict(name=row[0], type=row[1], dosage=row[2], ingredients=row[3], administration=row[4],
                 adverse_effects=row[5]) for row in medications
        ] if medications else None

    def create(self, medication_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO medications (name, description, dosage, duration, doctor_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (medication_data['name'], medication_data['description'], medication_data['dosage'],
              medication_data['duration'], medication_data['doctor_id']))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        return new_id

    def update(self, medication_id, medication_data):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE medications
            SET name = ?, description = ?, dosage = ?, duration = ?, doctor_id = ?
            WHERE id = ?
        ''', (medication_data['name'], medication_data['description'], medication_data['dosage'],
              medication_data['duration'], medication_data['doctor_id'], medication_id))
        conn.commit()
        rows_updated = cursor.rowcount
        conn.close()
        return rows_updated > 0

    def delete(self, medication_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM medications WHERE id = ?', (medication_id,))
        conn.commit()
        rows_deleted = cursor.rowcount
        conn.close()
        return rows_deleted > 0
