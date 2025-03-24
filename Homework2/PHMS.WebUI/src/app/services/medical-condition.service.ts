import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MedicalCondition } from '../models/medicalCondition.model';
import { Medication } from '../models/medication.model'; // Importați modelul Medication
import { Treatment } from '../models/treatment.model';

@Injectable({
  providedIn: 'root'
})
export class MedicalConditionService {
  private apiURL = 'http://localhost:5210/api/v1/MedicalCondition';
  private medicationApiURL = 'http://localhost:5210/api/v1/Medication'; // URL-ul pentru medicamente
  private treatmentApiURL = 'http://localhost:5210/api/v1/Treatment';

  constructor(private http: HttpClient) { }

  getMedicalConditionsByPatientId(patientId: string): Observable<MedicalCondition[]> {
    return this.http.get<MedicalCondition[]>(`${this.apiURL}/patient/${patientId}`);
  }

  createMedicalCondition(condition: MedicalCondition): Observable<any> {
    return this.http.post<MedicalCondition>(this.apiURL, condition);
  }

  addMedication(medication: any): Observable<any> {
    return this.http.post(this.medicationApiURL, medication);
  }

  generateMedications(conditionName: string): Observable<Medication[]> {
    return this.http.get<Medication[]>(`${this.medicationApiURL}/external/${conditionName}`);
  }

  addTreatment(treatment: any): Observable<any> {
    return this.http.post(this.treatmentApiURL, treatment);
    
  }

  deleteMedication(medicationId: string): Observable<void> {
    return this.http.delete<void>(`${this.medicationApiURL}/${medicationId}`);
  }
  
  addCondition(condition: any): Observable<any> {
    return this.http.post(`${this.apiURL}`, condition);
  }
}