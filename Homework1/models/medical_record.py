class MedicalRecord:
    def __init__(self, id, patient_id, disease_id , treatment_id, record_date, notes):
        self.id = id
        self.patient_id = patient_id
        self.disease_id = disease_id
        self.treatment_id = treatment_id
        self.record_date = record_date
        self.notes = notes

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'disease_id': self.disease_id,
            'treatment_id': self.treatment_id,
            'record_date': self.record_date,
            'notes': self.notes
        }