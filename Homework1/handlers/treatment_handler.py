from http.server import BaseHTTPRequestHandler
import json
from repositories.treatment_repository import TreatmentRepository
from urllib.parse import unquote

class TreatmentHandler(BaseHTTPRequestHandler):
    def __init__(self,request_handler):
        self.request_handler = request_handler
        self.treatment_repo = TreatmentRepository()

    def _send_response(self,status_code,data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type','application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        path = self.request_handler.path
        if path == '/treatments':
            self.get_treatments()
        elif path.startswith('/treatments/'):
            self.get_treatment_by_id()

    def get_treatments(self):
        treatments = self.treatment_repo.get_all()
        self._send_response(200,treatments)

    def get_treatment_by_id(self):
        treatment_id = self.request_handler.path.split('/')[-1]
        treatment = self.treatment_repo.get_by_id(treatment_id)
        if treatment:
            self._send_response(200,treatment)
        else:
            self._send_response(404,{'error':'Treatment not found'})

    def do_POST(self):
        content_length = int(self.request_handler.headers['Content-Length'])
        post_data = self.request_handler.rfile.read(content_length)
        new_treatment = json.loads(post_data.decode('utf-8'))

        new_id = self.treatment_repo.create(new_treatment)
        self._send_response(201,{'message':'Treatment created','id':new_id})

    def do_PUT(self):
        path = self.request_handler.path
        if path.startswith('/treatments/'):
            treatment_id = unquote(path.split('/')[-1])
            content_length = int(self.request_handler.headers['Content-Length'])
            put_data = self.request_handler.rfile.read(content_length)
            updated_treatment = json.loads(put_data.decode('utf-8'))

            success = self.treatment_repo.update(treatment_id,updated_treatment)
            if success:
                self._send_response(200,{'message':'Treatment updated'})
            else:
                self._send_response(404,{'error':'Treatment not found'})

    def do_DELETE(self):
        path = self.request_handler.path
        if path.startswith('/treatments/'):
            treatment_id = path.split('/')[-1]
            success = self.treatment_repo.delete(treatment_id)
            if success:
                self._send_response(200,{'message':'Treatment deleted'})
            else:
                self._send_response(404,{'error':'Treatment not found'})
