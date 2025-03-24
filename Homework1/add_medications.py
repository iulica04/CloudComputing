import sqlite3
import os

# Path to the database file
db_path = os.path.join(os.path.dirname(__file__), 'medical_system.db')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List of medications to add
medications = [
    ('Aspirin', 'Pain', 'Analgesic', '500mg', 'Acetylsalicylic Acid', 'Oral', 'Nausea, Vomiting'),
    ('Ibuprofen', 'Inflammation', 'NSAID', '200mg', 'Ibuprofen', 'Oral', 'Stomach pain, Heartburn'),
    ('Amoxicillin', 'Infection', 'Antibiotic', '250mg', 'Amoxicillin', 'Oral', 'Diarrhea, Rash'),
    ('Metformin', 'Diabetes', 'Antidiabetic', '500mg', 'Metformin', 'Oral', 'Nausea, Vomiting'),
    ('Lisinopril', 'Hypertension', 'ACEInhibitor', '10mg', 'Lisinopril', 'Oral', 'Dizziness, Cough'),
    ('Paracetamol', 'Pain', 'Analgesic', '500mg', 'Paracetamol', 'Oral', 'Liver damage, Nausea'),
    ('Cetirizine', 'Allergy', 'Antihistamine', '10mg', 'Cetirizine', 'Oral', 'Drowsiness, Dry mouth'),
    ('Atorvastatin', 'Cholesterol', 'Statin', '20mg', 'Atorvastatin', 'Oral', 'Muscle pain, Liver issues'),
    ('Omeprazole', 'Acid reflux', 'ProtonPumpInhibitor', '40mg', 'Omeprazole', 'Oral', 'Headache, Nausea'),
    ('Simvastatin', 'Cholesterol', 'Statin', '10mg', 'Simvastatin', 'Oral', 'Muscle pain, Weakness'),
    ('Losartan', 'Hypertension', 'ARB', '50mg', 'Losartan', 'Oral', 'Dizziness, Fatigue'),
    ('Ciprofloxacin', 'Infection', 'Antibiotic', '500mg', 'Ciprofloxacin', 'Oral', 'Nausea, Dizziness'),
    ('Doxycycline', 'Infection', 'Antibiotic', '100mg', 'Doxycycline', 'Oral', 'Sun sensitivity, Nausea'),
    ('Prednisone', 'Inflammation', 'Corticosteroid', '10mg', 'Prednisone', 'Oral', 'Weight gain, Insomnia'),
    ('Hydrochlorothiazide', 'Hypertension', 'Diuretic', '25mg', 'Hydrochlorothiazide', 'Oral', 'Dehydration, Dizziness'),
    ('Gabapentin', 'Neuropathy', 'Anticonvulsant', '300mg', 'Gabapentin', 'Oral', 'Drowsiness, Dizziness'),
    ('Alprazolam', 'Anxiety', 'Benzodiazepine', '0.5mg', 'Alprazolam', 'Oral', 'Drowsiness, Dependency'),
    ('Fluoxetine', 'Depression', 'SSRI', '20mg', 'Fluoxetine', 'Oral', 'Nausea, Insomnia'),
    ('Sertraline', 'Depression', 'SSRI', '50mg', 'Sertraline', 'Oral', 'Dizziness, Dry mouth'),
    ('Warfarin', 'Blood clot', 'Anticoagulant', '5mg', 'Warfarin', 'Oral', 'Bleeding, Bruising'),
    ('Ranitidine', 'Acid reflux', 'H2Blocker', '150mg', 'Ranitidine', 'Oral', 'Headache, Dizziness'),
    ('Clopidogrel', 'Heart disease', 'Antiplatelet', '75mg', 'Clopidogrel', 'Oral', 'Bleeding, Bruising'),
    ('Morphine', 'Pain', 'Opioid', '10mg', 'Morphine', 'Oral', 'Drowsiness, Addiction risk'),
    ('Codeine', 'Cough', 'Opioid', '30mg', 'Codeine', 'Oral', 'Constipation, Drowsiness'),
    ('Furosemide', 'Edema', 'Diuretic', '40mg', 'Furosemide', 'Oral', 'Dehydration, Low potassium'),
    ('Insulin', 'Diabetes', 'Hormone', 'Units Varies', 'Insulin', 'Injection', 'Hypoglycemia, Weight gain'),
    ('Levothyroxine', 'Hypothyroidism', 'Hormone', '50mcg', 'Levothyroxine', 'Oral', 'Palpitations, Weight loss'),
    ('Diazepam', 'Anxiety', 'Benzodiazepine', '5mg', 'Diazepam', 'Oral', 'Drowsiness, Dependency'),
    ('Naproxen', 'Inflammation', 'NSAID', '250mg', 'Naproxen', 'Oral', 'Stomach pain, Nausea'),
    # Adaugă mai multe înregistrări aici până la 100+...
]


# Insert medications into the database
for medication in medications:
    cursor.execute('''
        INSERT INTO medications (name, for_disease, type, dosage, ingredients, administration, adverse_effects)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', medication)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Medications added successfully!")