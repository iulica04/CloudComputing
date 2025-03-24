import json
from urllib.parse import unquote

from repositories.medication_repository import MedicationRepository


class MedicationHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.medication_repo = MedicationRepository()

    def _send_response(self, status_code, data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.request_handler.path == '/medications':
            self.get_medications()
        elif self.request_handler.path.startswith('/medications/disease/'):
            self.get_medications_by_disease()
        elif self.request_handler.path.startswith('/medications/'):
            self.get_medication_by_id()


    def get_medications(self):
        try:
            medications = self.medication_repo.get_all()
            self._send_response(200, medications)
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching medications: {str(e)}'})

    def get_medication_by_id(self):
        try:
            medication_id = self.request_handler.path.split('/')[-1]
            medication = self.medication_repo.get_by_id(medication_id)
            if medication:
                self._send_response(200, medication)
            else:
                self._send_response(404, {'error': 'Medication not found'})
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching medication by ID: {str(e)}'})

    def get_medications_by_disease(self):
        try:
            disease = self.request_handler.path.split('/')[-1]
            medications = self.medication_repo.get_by_disease_type(disease)
            if medications:
                self._send_response(200, medications)
            else:
                self._send_response(404, {'error': 'No medications found for this disease'})
        except Exception as e:
            self._send_response(500, {'error': f'Error fetching medications by disease: {str(e)}'})

    def do_POST(self):
        try:
            content_length = int(self.request_handler.headers['Content-Length'])
            post_data = self.request_handler.rfile.read(content_length)
            new_medication = json.loads(post_data.decode('utf-8'))

            new_id = self.medication_repo.create(new_medication)
            self._send_response(201, {'message': 'Medication created', 'id': new_id})
        except Exception as e:
            self._send_response(500, {'error': f'Error creating medication: {str(e)}'})


    def do_PUT(self):
        try:
            path = self.request_handler.path
            if path.startswith('/medications/'):
                medication_id = unquote(path.split('/')[-1])
                content_length = int(self.request_handler.headers['Content-Length'])
                put_data = self.request_handler.rfile.read(content_length)
                updated_medication = json.loads(put_data.decode('utf-8'))

                success = self.medication_repo.update(medication_id, updated_medication)
                if success:
                    self._send_response(200, {'message': 'Medication updated'})
                else:
                    self._send_response(404, {'error': 'Medication not found'})
        except Exception as e:
            self._send_response(500, {'error': f'Error updating medication: {str(e)}'})


    def do_DELETE(self):
        try:
            if self.request_handler.path.startswith('/medications/'):
                medication_id = self.request_handler.path.split('/')[-1]
                success = self.medication_repo.delete(medication_id)
                if success:
                    self._send_response(200, {'message': 'Medication deleted'})
                else:
                    self._send_response(404, {'error': 'Medication not found'})
        except Exception as e:
            self._send_response(500, {'error': f'Error deleting medication: {str(e)}'})