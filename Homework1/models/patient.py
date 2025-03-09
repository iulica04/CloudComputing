class Patient:
    def __init__(self, id, first_name, last_name, cnp, date_of_birth, gender, phone, email, address):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.cnp = cnp
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "cnp": self.cnp,
            "date_of_birth": self.date_of_birth,
            'gender': self.gender,
            'phone': self.phone,
            'email': self.email,
            'address': self.address
        }
