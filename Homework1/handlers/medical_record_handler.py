import json
from repositories.medical_record_repository import MedicalRecordRepository
from repositories.patient_repository import PatientRepository
from urllib.parse import unquote

class MedicalRecordHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.medical_record_repo = MedicalRecordRepository()

    def _send_response(self, status_code, data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        path = self.request_handler.path
        if path == '/medical_records':
            self.get_medical_records()
        elif path.startswith('/medical_records/'):
            if 'patient' in path:
                self.get_medical_records_for_patient()
            elif 'disease' in path:
                self.get_medical_records_by_disease()
            else:
                self.get_medical_record_by_id()

    def get_medical_records_for_patient(self):
        try:
            path = self.request_handler.path
            patient_id = unquote(path.split('/')[-1])
            medical_records = self.medical_record_repo.get_by_patient_id(patient_id)
            if medical_records:
                self._send_response(200, medical_records)
            else:
                self._send_response(404, {'error': 'No medical records found for this patient'})
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching medical records for patient: {str(e)}'})

    def get_medical_records_for_disease(self):
        try:
            path = self.request_handler.path
            disease_id = unquote(path.split('/')[-1])
            medical_records = self.medical_record_repo.get_by_disease_id(disease_id)

            if medical_records:
                self._send_response(200, medical_records)
            else:
                self._send_response(404, {'error': 'No medical records found for this disease'})
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching medical records for disease: {str(e)}'})

    def get_medical_records(self):
        medical_records = self.medical_record_repo.get_all()
        self._send_response(200, medical_records)

    def get_medical_record_by_id(self):
        medical_record_id = self.request_handler.path.split('/')[-1]
        medical_record = self.medical_record_repo.get_by_id(medical_record_id)
        if medical_record:
            self._send_response(200, medical_record)
        else:
            self._send_response(404, {'error': 'Medical record not found'})

    def get_medical_records_by_disease(self):
        try:
            path= self.request_handler.path
            disease_id = unquote(path.split('/')[-1])
            medical_records = self.medical_record_repo.get_by_disease_id(disease_id)
            if medical_records:
                self._send_response(200, medical_records)
            else:
                self._send_response(404, {'error': 'No medical records found for this disease'})
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching medical records for disease: {str(e)}'})

    def do_POST(self):
        content_length = int(self.request_handler.headers['Content-Length'])
        post_data = self.request_handler.rfile.read(content_length)
        new_medical_record = json.loads(post_data.decode('utf-8'))

        new_id, error = self.medical_record_repo.create(new_medical_record)
        if error:
            self._send_response(400, {'error': error})
        else:
            self._send_response(201, {'message': 'Medical record created', 'id': new_id})

    def do_PUT(self):
        path = self.request_handler.path
        if path.startswith('/medical_records/'):
            medical_record_id = unquote(path.split('/')[-1])
            content_length = int(self.request_handler.headers['Content-Length'])
            put_data = self.request_handler.rfile.read(content_length)
            updated_medical_record = json.loads(put_data.decode('utf-8'))

            success, error = self.medical_record_repo.update(medical_record_id, updated_medical_record)
            if success:
                self._send_response(200, {'message': 'Medical record updated'})
            else:
                self._send_response(404, {'error': error})

    def do_DELETE(self):
        path = self.request_handler.path
        if path.startswith('/medical_records/'):
            medical_record_id = path.split('/')[-1]
            success = self.medical_record_repo.delete(medical_record_id)
            if success:
                self._send_response(200, {'message': 'Medical record deleted'})
            else:
                self._send_response(404, {'error': 'Medical record not found'})
