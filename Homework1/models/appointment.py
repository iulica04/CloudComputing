class Appointment:
    def __init__(self, id, patient_id, doctor_id, appointment_date, purpose):
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.purpose = purpose

    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'doctor_id': self.doctor_id,
            'appointment_date': self.appointment_date,
            'purpose': self.purpose
        }