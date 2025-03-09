class Doctor:
    def __init__(self, id, first_name, last_name, specialization, phone, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'specialization': self.specialization,
            'phone': self.phone,
            'email': self.email
        }