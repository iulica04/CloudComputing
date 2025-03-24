import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Patient } from '../../models/patient.model';
import { PatientService } from '../../services/patient.service';
import { Router } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-patient-list',
  standalone: true,
  imports: [CommonModule, NavbarComponent],
  templateUrl: './patient-list.component.html',
  styleUrls: ['./patient-list.component.css']
})
export class PatientListComponent implements OnInit {
  
  patients: Patient[] = [];
  constructor(private patientService: PatientService, private router: Router) {}
  
  ngOnInit(): void {
    this.patientService.getPatients().subscribe((data: Patient[]) => {
      this.patients = data;
    });
  }

  navigateToMedicalCondition(id: string): void {
    this.router.navigate([`/medical-condition/${id}`]);
  }

  logout(): void {
    this.patientService.logout();
  }
}