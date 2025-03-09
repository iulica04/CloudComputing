class Treatment:
    def __init__(self, id, name, description, dosage, duration, doctor_id):
        self.id = id
        self.name = name
        self.description = description
        self.dosage = dosage
        self.duration = duration
        self.doctor_id = doctor_id

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'dosage': self.dosage,
            'duration': self.duration,
            'doctor_id': self.doctor_id
        }