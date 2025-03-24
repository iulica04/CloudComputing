import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MedicalConditionService } from '../../services/medical-condition.service';
import { NavbarComponent } from '../navbar/navbar.component';
import { TreatmentType, Treatment } from '../../models/treatment.model';
import { MedicationType, Medication } from '../../models/medication.model';
import { MedicalCondition } from '../../models/medicalCondition.model';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-medical-condition-for-patient',
  standalone: true,
  imports: [CommonModule, NavbarComponent, ReactiveFormsModule, FormsModule],
  templateUrl: './medical-condition-for-patient.component.html',
  styleUrls: ['./medical-condition-for-patient.component.css']
})
export class MedicalConditionForPatientComponent implements OnInit {
  medicalConditions: MedicalCondition[] = [];
  patientId: string = '';
  showAddMedicationForm: boolean = false;
  showAddTreatmentForm: boolean = false;
  showAddConditionForm: boolean = false;
  medicationForm: FormGroup;
  treatmentForm: FormGroup;
  conditionForm: FormGroup;
  medicationTypes: { value: number; name: string }[] = [];
  treatmentTypes: { value: number; name: string }[] = [];
  generatedMedications: Medication[] = [];
  currentMedicationIndex: number = 0;
  conditionName: string = '';



  constructor(
    private route: ActivatedRoute,
    private medicalConditionService: MedicalConditionService,
    private fb: FormBuilder,
    private router: Router
  ) {
    this.medicationForm = this.fb.group({
      name: ['', Validators.required],
      type: ['', Validators.required],
      dosage: ['', Validators.required],
      administration: ['', Validators.required],
      ingredients: ['', Validators.required],
      adverseEffects: ['', Validators.required]
    });

    this.treatmentForm = this.fb.group({
      name: ['', Validators.required],
      type: ['', Validators.required],
      location: ['', Validators.required],
      startDate: ['', Validators.required],
      duration: ['', Validators.required]
    });

    this.conditionForm = this.fb.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      startDate: ['', Validators.required],
      endDate: [''], // Adăugat câmpul endDate
      currentStatus: ['', Validators.required],
      isGenetic: [false],
      recommendation: ['']
    });
  }

  ngOnInit(): void {
    this.patientId = this.route.snapshot.paramMap.get('id')!;
    this.medicalConditionService.getMedicalConditionsByPatientId(this.patientId).subscribe((data: MedicalCondition[]) => {
      this.medicalConditions = data;
    });

    // Populați array-ul `medicationTypes` cu numele și valorile enum-ului
    this.medicationTypes = Object.keys(MedicationType)
      .filter(key => isNaN(Number(key))) // Exclude valorile numerice
      .map(key => ({
        value: MedicationType[key as keyof typeof MedicationType],
        name: key
      }));

    // Populați array-ul `treatmentTypes` cu numele și valorile enum-ului
    this.treatmentTypes = Object.keys(TreatmentType)
      .filter(key => isNaN(Number(key))) // Exclude valorile numerice
      .map(key => ({
        value: TreatmentType[key as keyof typeof TreatmentType],
        name: key
      }));
  }

  getTreatmentType(type: TreatmentType): string {
    switch (type) {
      case TreatmentType.Surgery:
        return 'Surgery';
      case TreatmentType.Therapy:
        return 'Therapy';
      case TreatmentType.Medication:
        return 'Medication';
      case TreatmentType.Rehabilitation:
        return 'Rehabilitation';
      case TreatmentType.Other:
        return 'Other';
      default:
        return 'Unknown';
    }
  }

  getMedicationType(type: MedicationType): string {
    return MedicationType[type];
  }

  formatDuration(duration: string): string {
    const date = new Date(duration);
    return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`;
  }

  toggleAddMedicationForm(): void {
    this.showAddMedicationForm = !this.showAddMedicationForm;
  }

  toggleAddTreatmentForm(): void {
    this.showAddTreatmentForm = !this.showAddTreatmentForm;
  }

  toggleAddConditionForm(): void {
    this.showAddConditionForm = !this.showAddConditionForm;
  }

  addCondition(): void {
    if (this.conditionForm.valid) {
      const newCondition: any = {
        patientId: this.patientId, // Adăugat ID-ul pacientului
        name: this.conditionForm.value.name,
        description: this.conditionForm.value.description,
        startDate: this.conditionForm.value.startDate
          ? new Date(this.conditionForm.value.startDate).toISOString()
          : null,
        endDate: this.conditionForm.value.endDate
          ? new Date(this.conditionForm.value.endDate).toISOString()
          : null,
        currentStatus: this.conditionForm.value.currentStatus,
        isGenetic: this.conditionForm.value.isGenetic,
        recommendation: this.conditionForm.value.recommendation || null,
        treatments: [] // Inițial, lista de tratamente este goală
      };

      this.medicalConditionService.addCondition(newCondition).subscribe(
        response => {
          console.log('New Condition added:', response);
          this.toggleAddConditionForm();
          this.medicalConditions.push(response); // Adăugați boala în lista locală
          location.reload();
        },
        error => {
          console.error('Error adding condition:', error);
        }
      );
    }
  }

  addMedication(treatmentId: string): void {
    if (this.medicationForm.valid) {
      const newMedication: any = {
        treatmentId: treatmentId,
        name: this.medicationForm.value.name,
        type: Number(this.medicationForm.value.type),
        dosage: this.medicationForm.value.dosage,
        administration: this.medicationForm.value.administration,
        ingredients: this.medicationForm.value.ingredients,
        adverseEffects: this.medicationForm.value.adverseEffects
      };
  
      this.medicalConditionService.addMedication(newMedication).subscribe(
        response => {
          console.log('New Medication added:', response);
          this.toggleAddMedicationForm();
          const condition = this.medicalConditions.find(condition => condition.treatments.some((t: Treatment) => t.treatmentId === treatmentId));
          if (condition) {
            const treatment = condition.treatments.find((t: Treatment) => t.treatmentId === treatmentId);
            if (treatment) {
              treatment.medications.push(response);
            }
          }
          location.reload();
        },
        error => {
          console.error('Error adding medication:', error);
        }
      );
    }
  }

  addTreatment(conditionId: string): void {
    if (this.treatmentForm.valid) {
      const startDateValue = this.treatmentForm.value.startDate;
      const durationValue = this.treatmentForm.value.duration;
  
      // Verificați dacă valorile sunt valide
      if (!startDateValue || isNaN(new Date(startDateValue).getTime())) {
        console.error('Invalid start date');
        console.log('Please enter a valid start date.');
        return;
      }
  
     
  
      const newTreatment = {
        type: Number(this.treatmentForm.value.type), // Tipul tratamentului (numeric)
        name: this.treatmentForm.value.name, // Numele tratamentului
        medicalConditionId: conditionId, // ID-ul afecțiunii medicale
        location: this.treatmentForm.value.location, // Locația tratamentului
        startDate: new Date(startDateValue).toISOString(), // Data de început în format ISO
        duration: new Date(durationValue).toISOString(), // Durata în format ISO
        medications: [] // Lista de medicamente (inițial goală)
      };

  
      // Apelați serviciul pentru a adăuga tratamentul
      this.medicalConditionService.addTreatment(newTreatment).subscribe(
        response => {
          console.log('New Treatment added:', response);
          this.toggleAddTreatmentForm();
          const condition = this.medicalConditions.find(c => c.medicalConditionId === conditionId);
          if (condition) {
            condition.treatments.push(response);
          }
          location.reload();
        },
        error => {
          console.error('Error adding treatment:', error);
        }
      );
    }
  }

  generateMedications(): void {
    if (!this.conditionName.trim()) {
      alert('Please enter a condition name.');
      return;
    }

    this.medicalConditionService.generateMedications(this.conditionName).subscribe((medications: Medication[]) => {
      this.generatedMedications = medications;
      this.currentMedicationIndex = 0;
      this.fillMedicationForm(this.generatedMedications[this.currentMedicationIndex]);
    });
  }

  fillMedicationForm(medication: Medication): void {
    this.medicationForm.patchValue({
      name: medication.name,
      type: medication.type,
      dosage: medication.dosage,
      administration: medication.administration,
      ingredients: medication.ingredients,
      adverseEffects: medication.adverseEffects
    });
  }

  nextMedication(): void {
    if (this.currentMedicationIndex < this.generatedMedications.length - 1) {
      this.currentMedicationIndex++;
      this.fillMedicationForm(this.generatedMedications[this.currentMedicationIndex]);
    }
  }

  previousMedication(): void {
    if (this.currentMedicationIndex > 0) {
      this.currentMedicationIndex--;
      this.fillMedicationForm(this.generatedMedications[this.currentMedicationIndex]);
    }
  }

  deleteMedication(medicationId: string, treatmentId: string): void {
    if (confirm('Are you sure you want to delete this medication?')) {
      this.medicalConditionService.deleteMedication(medicationId).subscribe(
        () => {
          const treatment = this.medicalConditions
            .flatMap(condition => condition.treatments)
            .find(t => t.treatmentId === treatmentId);
  
          if (treatment) {
            treatment.medications = treatment.medications.filter(m => m.id !== medicationId);
          }
          console.log('Medication deleted successfully');
        },
        error => {
          console.error('Error deleting medication:', error);
        }
      );
    }
  }
}