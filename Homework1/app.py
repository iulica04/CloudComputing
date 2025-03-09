from http.server import BaseHTTPRequestHandler, HTTPServer

from handlers.appointment_handler import AppointmentHandler
from handlers.disease_handler import DiseaseHandler
from handlers.medical_record_handler import MedicalRecordHandler
from handlers.patient_handler import PatientHandler
from handlers.doctor_handler import DoctorHandler
from handlers.treatment_handler import TreatmentHandler


class Router(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/patients"):
            handler = PatientHandler(self)
            handler.do_GET()
        elif self.path.startswith("/doctors"):
            handler = DoctorHandler(self)
            handler.do_GET()
        elif self.path.startswith("/appointments"):
            handler = AppointmentHandler(self)
            handler.do_GET()
        elif self.path.startswith("/diseases"):
            handler = DiseaseHandler(self)
            handler.do_GET()
        elif self.path.startswith("/treatments"):
            handler = TreatmentHandler(self)
            handler.do_GET()
        elif self.path.startswith("/medical_records"):
            handler = MedicalRecordHandler(self)
            handler.do_GET()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def do_POST(self):
        if self.path.startswith("/patients"):
            handler = PatientHandler(self)
            handler.do_POST()
        elif self.path.startswith("/doctors"):
            handler = DoctorHandler(self)
            handler.do_POST()
        elif self.path.startswith("/appointments"):
            handler = AppointmentHandler(self)
            handler.do_POST()
        elif self.path.startswith("/diseases"):
            handler = DiseaseHandler(self)
            handler.do_POST()
        elif self.path.startswith("/treatments"):
            handler = TreatmentHandler(self)
            handler.do_POST()
        elif self.path.startswith("/medical_records"):
            handler = MedicalRecordHandler(self)
            handler.do_POST()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def do_PUT(self):
        if self.path.startswith("/patients"):
            handler = PatientHandler(self)
            handler.do_PUT()
        elif self.path.startswith("/doctors"):
            handler = DoctorHandler(self)
            handler.do_PUT()
        elif self.path.startswith("/appointments"):
            handler = AppointmentHandler(self)
            handler.do_PUT()
        elif self.path.startswith("/diseases"):
            handler = DiseaseHandler(self)
            handler.do_PUT()
        elif self.path.startswith("/treatments"):
            handler = TreatmentHandler(self)
            handler.do_PUT()
        elif self.path.startswith("/medical_records"):
            handler = MedicalRecordHandler(self)
            handler.do_PUT()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def do_DELETE(self):
        if self.path.startswith("/patients"):
            handler = PatientHandler(self)
            handler.do_DELETE()
        elif self.path.startswith("/doctors"):
            handler = DoctorHandler(self)
            handler.do_DELETE()
        elif self.path.startswith("/appointments"):
            handler = AppointmentHandler(self)
            handler.do_DELETE()
        elif self.path.startswith("/diseases"):
            handler = DiseaseHandler(self)
            handler.do_DELETE()
        elif self.path.startswith("/treatments"):
            handler = TreatmentHandler(self)
            handler.do_DELETE()
        elif self.path.startswith("/medical_records"):
            handler = MedicalRecordHandler(self)
            handler.do_DELETE()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

def run(server_class=HTTPServer, handler_class=Router, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
