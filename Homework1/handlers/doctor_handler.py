import json
from repositories.doctor_repository import DoctorRepository
from urllib.parse import unquote

class DoctorHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.doctor_repo = DoctorRepository()

    def _send_response(self, status_code, data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        if self.request_handler.path == "/doctors":
            self.get_doctors()
        elif self.request_handler.path.startswith("/doctors/"):
            self.get_doctor_by_id()

    def get_doctors(self):
        doctors = self.doctor_repo.get_all()
        self._send_response(200, doctors)

    def get_doctor_by_id(self):
        doctor_id = self.request_handler.path.split("/")[-1]
        doctor = self.doctor_repo.get_by_id(doctor_id)
        if doctor:
            self._send_response(200, doctor)
        else:
            self._send_response(404, {"error": "Doctor not found"})

    def do_POST(self):
        content_length = int(self.request_handler.headers["Content-Length"])
        post_data = self.request_handler.rfile.read(content_length)
        new_doctor = json.loads(post_data.decode("utf-8"))

        new_id = self.doctor_repo.create(new_doctor)
        self._send_response(201, {"message": "Doctor created", "id": new_id})

    def do_PUT(self):
        path = self.request_handler.path
        if path.startswith("/doctors/"):
            doctor_id = unquote(path.split('/')[-1])
            content_length = int(self.request_handler.headers["Content-Length"])
            put_data = self.request_handler.rfile.read(content_length)
            updated_doctor = json.loads(put_data.decode("utf-8"))

            success = self.doctor_repo.update(doctor_id, updated_doctor)
            if success:
                self._send_response(200, {"message": "Doctor updated"})
            else:
                self._send_response(404, {"error": "Doctor not found"})

    def do_DELETE(self):
        if self.request_handler.path.startswith("/doctors/"):
            doctor_id = self.request_handler.path.split("/")[-1]
            success = self.doctor_repo.delete(doctor_id)
            if success:
                self._send_response(200, {"message": "Doctor deleted"})
            else:
                self._send_response(404, {"error": "Doctor not found"})
