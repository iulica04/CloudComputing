from http.server import BaseHTTPRequestHandler
import json
from repositories.appointment_repository import AppointmentRepository
from urllib.parse import unquote

class AppointmentHandler:
    def __init__(self, request_handler):
        self.request_handler = request_handler
        self.appointment_repo = AppointmentRepository()

    def _send_response(self, status_code, data=None):
        self.request_handler.send_response(status_code)
        self.request_handler.send_header('Content-type', 'application/json')
        self.request_handler.end_headers()
        if data:
            self.request_handler.wfile.write(json.dumps(data).encode('utf-8'))

    def do_GET(self):
        path = self.request_handler.path
        if path == '/appointments':
            self.get_appointments()
        elif path.startswith('/appointments/'):
            if 'patient' in path:
                self.get_appointments_for_patient()
            else:
                self.get_appointment_by_id()

    def get_appointments_for_patient(self):
        path = self.request_handler.path
        patient_id = unquote(path.split('/')[-1])
        appointments = self.appointment_repo.get_by_patient_id(patient_id)
        if appointments:
            self._send_response(200, appointments)
        else:
            self._send_response(404, {'error': 'No appointments found for this patient'})

    def get_appointments(self):
        appointments = self.appointment_repo.get_all()
        self._send_response(200, appointments)

    def get_appointment_by_id(self):
        appointment_id = self.request_handler.path.split('/')[-1]
        appointment = self.appointment_repo.get_by_id(appointment_id)
        if appointment:
            self._send_response(200, appointment)
        else:
            self._send_response(404, {'error': 'Appointment not found'})

    def do_POST(self):
        content_length = int(self.request_handler.headers['Content-Length'])
        post_data = self.request_handler.rfile.read(content_length)
        new_appointment = json.loads(post_data.decode('utf-8'))

        new_id, error= self.appointment_repo.create(new_appointment)
        if ("Patient ID not found" in error) or ("Doctor ID not found" in error):
            self._send_response(404, {'error': error})
        elif error:
            self._send_response(400, {'error':error})
        else:
            self._send_response(201, {'message': 'Appointment created', 'id': new_id})

    def do_PUT(self):
        path = self.request_handler.path
        if path.startswith('/appointments/'):
            appointment_id = unquote(path.split('/')[-1])
            content_length = int(self.request_handler.headers['Content-Length'])
            put_data = self.request_handler.rfile.read(content_length)
            updated_appointment = json.loads(put_data.decode('utf-8'))

            success, error = self.appointment_repo.update(appointment_id, updated_appointment)
            if success:
                self._send_response(200, {'message': 'Appointment updated'})
            else:
                if ("Patient ID not found" in error) or ("Doctor ID not found" in error) or ("Appointment ID not found" in error):
                    self._send_response(404, {'error': error})
                elif error:
                    self._send_response(400, {'error': error})

    def do_DELETE(self):
        path = self.request_handler.path
        if path.startswith('/appointments/'):
            appointment_id = path.split('/')[-1]
            success = self.appointment_repo.delete(appointment_id)
            if success:
                self._send_response(200, {'message': 'Appointment deleted'})
            else:
                self._send_response(404, {'error': 'Appointment not found'})
