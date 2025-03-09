class Disease:
    def __init__(self, id, name, type, symptoms, severity):
        self.id = id
        self.name = name
        self.type = type
        self.symptoms = symptoms
        self.severity = severity

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'symptoms': self.symptoms,
            'severity': self.severity
        }