import { Component, OnInit, Input } from '@angular/core';
import { CommonModule, DatePipe } from '@angular/common';
import { MedicalCondition } from '../../models/medicalCondition.model';
import { MedicalConditionService } from '../../services/medical-condition.service';
import { TreatmentType } from '../../models/treatment.model';
import { MedicationType } from '../../models/medication.model';

@Component({
  selector: 'app-medical-condition-get',
  templateUrl: './medical-condition-get.component.html',
  styleUrls: ['./medical-condition-get.component.css'],
  standalone: true,
  imports: [CommonModule, DatePipe]
})
export class MedicalConditionGetComponent implements OnInit {
  @Input() patientId: string | null = null;
  medicalConditions: MedicalCondition[] = [];

  constructor(private medicalConditionService: MedicalConditionService) {}

  ngOnInit(): void {
    if (this.patientId) {
      this.medicalConditionService.getMedicalConditionsByPatientId(this.patientId).subscribe(
        (data: MedicalCondition[]) => {
          this.medicalConditions = data;
        },
        (error) => {
          console.error('Error fetching medical conditions:', error);
        }
      );
    }
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
    switch (type) {
      case MedicationType.Tablet:
        return 'Tablet';
      case MedicationType.Capsule:
        return 'Capsule';
      case MedicationType.Syrup:
        return 'Syrup';
      case MedicationType.Injection:
        return 'Injection';
      case MedicationType.Cream:
        return 'Cream';
      case MedicationType.Ointment:
        return 'Ointment';
      case MedicationType.Drops:
        return 'Drops';
      case MedicationType.Inhaler:
        return 'Inhaler';
      case MedicationType.Spray:
        return 'Spray';
      case MedicationType.Patch:
        return 'Patch';
      case MedicationType.Suppository:
        return 'Suppository';
      case MedicationType.Implant:
        return 'Implant';
      case MedicationType.Powder:
        return 'Powder';
      case MedicationType.Gel:
        return 'Gel';
      case MedicationType.Lotion:
        return 'Lotion';
      case MedicationType.Liquid:
        return 'Liquid';
      case MedicationType.Lozenge:
        return 'Lozenge';
      case MedicationType.Solution:
        return 'Solution';
      case MedicationType.Suspension:
        return 'Suspension';
      case MedicationType.Syringe:
        return 'Syringe';
      case MedicationType.Analgesic:
        return 'Analgesic';
      case MedicationType.NSAID:
        return 'NSAID';
      case MedicationType.Antibiotic:
        return 'Antibiotic';
      case MedicationType.Antidiabetic:
        return 'Antidiabetic';
      case MedicationType.ACEInhibitor:
        return 'ACE Inhibitor';
      case MedicationType.Antihistamine:
        return 'Antihistamine';
      case MedicationType.Statin:
        return 'Statin';
      case MedicationType.ProtonPumpInhibitor:
        return 'Proton Pump Inhibitor';
      case MedicationType.ARB:
        return 'ARB';
      case MedicationType.Corticosteroid:
        return 'Corticosteroid';
      case MedicationType.Diuretic:
        return 'Diuretic';
      case MedicationType.Anticonvulsant:
        return 'Anticonvulsant';
      case MedicationType.Benzodiazepine:
        return 'Benzodiazepine';
      case MedicationType.SSRI:
        return 'SSRI';
      case MedicationType.Anticoagulant:
        return 'Anticoagulant';
      case MedicationType.H2Blocker:
        return 'H2 Blocker';
      case MedicationType.Antiplatelet:
        return 'Antiplatelet';
      case MedicationType.Opioid:
        return 'Opioid';
      case MedicationType.Hormone:
        return 'Hormone';
      case MedicationType.Other:
        return 'Other';
      default:
        return 'Unknown';
    }
  }

  formatDuration(duration: string): string {
    const date = new Date(duration);
    return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`;
  }
}