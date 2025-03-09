import json
from urllib.parse import unquote
from repositories.patient_repository import PatientRepository

class PatientHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.patient_repo = PatientRepository()

    def _send_response(self, status_code, data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        try:
            path = self.request_handler.path
            if path == '/patients':
                self.get_patients()
            elif path.startswith('/patients/'):
                self.get_patient_by_id()
        except Exception as e:
            self._send_response(500, {'error': f'Internal Server Error: {str(e)}'})

    def get_patients(self):
        try:
            patients = self.patient_repo.get_all()
            self._send_response(200, patients)
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching patients: {str(e)}'})

    def get_patient_by_id(self):
        try:
            patient_id = self.request_handler.path.split('/')[-1]
            patient = self.patient_repo.get_by_id(patient_id)
            if patient:
                self._send_response(200, patient)
            else:
                self._send_response(404, {'error': 'Patient not found'})
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching patient by ID: {str(e)}'})

    def do_POST(self):
        try:
            content_length = int(self.request_handler.headers['Content-Length'])
            post_data = self.request_handler.rfile.read(content_length)
            new_patient = json.loads(post_data.decode('utf-8'))

            new_id = self.patient_repo.create(new_patient)
            self._send_response(201, {'message': 'Patient created', 'id': new_id})
        except Exception as e:
            self._send_response(500, {'error': f'Error creating patient: {str(e)}'})

    def do_PUT(self):
        try:
            path = self.request_handler.path
            if path.startswith('/patients/'):
                patient_id = unquote(path.split('/')[-1])
                content_length = int(self.request_handler.headers['Content-Length'])
                put_data = self.request_handler.rfile.read(content_length)
                updated_patient = json.loads(put_data.decode('utf-8'))

                success = self.patient_repo.update(patient_id, updated_patient)
                if success:
                    self._send_response(200, {'message': 'Patient updated'})
                else:
                    self._send_response(404, {'error': 'Patient not found'})
        except Exception as e:
            self._send_response(500, {'error': f'Error updating patient: {str(e)}'})

    def do_DELETE(self):
        try:
            path = self.request_handler.path
            if path.startswith('/patients/'):
                patient_id = path.split('/')[-1]
                success = self.patient_repo.delete(patient_id)
                if success:
                    self._send_response(200, {'message': 'Patient deleted'})
                else:
                    self._send_response(404, {'error': 'Patient not found'})
        except Exception as e:
            self._send_response(500, {'error': f'Error deleting patient: {str(e)}'})
