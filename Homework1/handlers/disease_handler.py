import json
from repositories.disease_repository import DiseaseRepository
from urllib.parse import unquote

class DiseaseHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.disease_repo = DiseaseRepository()

    def _send_response(self, status_code, data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.request_handler.path == '/diseases':
            self.get_diseases()
        elif self.request_handler.path.startswith('/diseases/'):
            self.get_disease_by_id()

    def get_diseases(self):
        diseases = self.disease_repo.get_all()
        self._send_response(200, diseases)

    def get_disease_by_id(self):
        disease_id = self.request_handler.path.split('/')[-1]
        disease = self.disease_repo.get_by_id(disease_id)
        if disease:
            self._send_response(200, disease)
        else:
            self._send_response(404, {'error': 'Disease not found'})

    def do_POST(self):
        content_length = int(self.request_handler.headers['Content-Length'])
        post_data = self.request_handler.rfile.read(content_length)
        new_disease = json.loads(post_data.decode('utf-8'))

        new_id = self.disease_repo.create(new_disease)
        self._send_response(201, {'message': 'Disease created', 'id': new_id})

    def do_PUT(self):
        path = self.request_handler.path
        if path.startswith('/diseases/'):
            disease_id = unquote(path.split('/')[-1])
            content_length = int(self.request_handler.headers['Content-Length'])
            put_data = self.request_handler.rfile.read(content_length)
            updated_disease = json.loads(put_data.decode('utf-8'))

            success = self.disease_repo.update(disease_id, updated_disease)
            if success:
                self._send_response(200, {'message': 'Disease updated'})
            else:
                self._send_response(404, {'error': 'Disease not found'})

    def do_DELETE(self):
        if self.request_handler.path.startswith('/diseases/'):
            disease_id = self.request_handler.path.split('/')[-1]
            success = self.disease_repo.delete(disease_id)
            if success:
                self._send_response(200, {'message': 'Disease deleted'})
            else:
                self._send_response(404, {'error': 'Disease not found'})
