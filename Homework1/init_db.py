import os
import sqlite3
import os
# Calea completă către fișierul clinic.db
db_path = os.path.join(os.path.dirname(__file__), 'medical_system.db')

# Conectare la baza de date (sau creare dacă nu există)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    ssn TEXT UNIQUE NOT NULL,
    date_of_birth TEXT NOT NULL,
    gender TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL
)
''')

# Creare tabelă doctors
cursor.execute('''
CREATE TABLE IF NOT EXISTS doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    specialization TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Creare tabelă diseases
cursor.execute('''
CREATE TABLE IF NOT EXISTS diseases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    type TEXT NOT NULL,
    symptoms TEXT NOT NULL,
    severity TEXT NOT NULL
)
''')

# Creare tabelă treatments
cursor.execute('''
CREATE TABLE IF NOT EXISTS treatments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    dosage TEXT NOT NULL,
    duration TEXT NOT NULL,
    doctor_id INTEGER NOT NULL,
    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
)
''')

# Creare tabelă medical_records
cursor.execute('''
CREATE TABLE IF NOT EXISTS medical_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    disease_id INTEGER NOT NULL,
    treatment_id INTEGER NOT NULL,
    record_date TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients (id),
    FOREIGN KEY (disease_id) REFERENCES diseases (id),
    FOREIGN KEY (treatment_id) REFERENCES treatments (id)
)
''')

# Creare tabelă appointments
cursor.execute('''
CREATE TABLE IF NOT EXISTS appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    appointment_date TEXT NOT NULL,
    purpose TEXT NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients (id),
    FOREIGN KEY (doctor_id) REFERENCES doctors (id)
)
''')

# Adaugă date inițiale (opțional)
cursor.execute("INSERT INTO patients (first_name, last_name, ssn, date_of_birth, gender, phone, email, address) VALUES ('John', 'Doe', '123-45-6789', '1990-01-01', 'Male', '123-456-7890', 'john.doe@example.com', '123 Main St')")
cursor.execute("INSERT INTO doctors (first_name, last_name, specialization, phone, email) VALUES ('Jane', 'Smith', 'Cardiologist', '987-654-3210', 'jane.smith@example.com')")
cursor.execute("INSERT INTO diseases (name, type, symptoms, severity) VALUES ('Flu', 'Acute', 'Fever, Cough', 'Medium')")
cursor.execute("INSERT INTO treatments (name, description, dosage, duration, doctor_id) VALUES ('Paracetamol', 'Fever reducer', '500mg', '7 days', 1)")
cursor.execute("INSERT INTO medical_records (patient_id, disease_id, treatment_id, record_date, notes) VALUES (1, 1, 1, '2023-10-01', 'Patient responded well to treatment')")
cursor.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, purpose) VALUES (1, 1, '2023-10-15', 'Follow-up')")

# Salvează modificările și închide conexiunea
conn.commit()
conn.close()

print("Database initialized successfully!")