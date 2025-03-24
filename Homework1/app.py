from http.server import BaseHTTPRequestHandler, HTTPServer
from handlers.appointment_handler import AppointmentHandler
from handlers.disease_handler import DiseaseHandler
from handlers.medical_record_handler import MedicalRecordHandler
from handlers.medication_handler import MedicationHandler
from handlers.patient_handler import PatientHandler
from handlers.doctor_handler import DoctorHandler
from handlers.treatment_handler import TreatmentHandler

API_KEY = "wxTurM17oUeeDpme90Etw4qMg9m5ymPao0PIkayB4nPQmYkH7SFwArAjnWvwcgxMmL6itctJQd78LN9BeqWfJ9cOi0PCc17zWHVRPHHtEfJUB5JCFoGydRwVNM0TkGOj"

def require_api_key_for_medications(handler_method):
    def wrapper(self, *args, **kwargs):
        # just for '/medications'
        if self.path.startswith("/medications"):
            api_key = self.headers.get('Authorization')
            if api_key != f'Bearer {API_KEY}':
                self.send_response(401)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"error": "Unauthorized"}')
                return
        return handler_method(self, *args, **kwargs)
    return wrapper

class Router(BaseHTTPRequestHandler):
    @require_api_key_for_medications
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
        elif self.path.startswith("/medications/disease/"):
            handler = MedicationHandler(self)
            handler.do_GET()
        elif self.path.startswith("/medications"):
            handler = MedicationHandler(self)
            handler.do_GET()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    @require_api_key_for_medications
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
        elif self.path.startswith("/medications"):
            handler = MedicationHandler(self)
            handler.do_POST()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    @require_api_key_for_medications
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
        elif self.path.startswith("/medications"):
            handler = MedicationHandler(self)
            handler.do_PUT()
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    @require_api_key_for_medications
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
        elif self.path.startswith("/medications"):
            handler = MedicationHandler(self)
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
