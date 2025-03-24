import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-specializations',
  standalone: true,
  imports: [CommonModule, NavbarComponent],
  templateUrl: './specializations.component.html',
  styleUrls: ['./specializations.component.css']
})
export class SpecializationsComponent {
  specializations: string[] = [
    'Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'Dermatology', 'Oncology', 'Gastroenterology', 
    'Urology', 'Psychiatry', 'Internal Medicine', 'Endocrinology', 'Hematology', 'Infectious Diseases', 
    'Geriatrics', 'Immunology', 'Radiology', 'Rheumatology', 'Rehabilitation Medicine', 'Sports Medicine', 
    'Intensive Care Medicine', 'Toxicology', 'Genetics', 'Nutrition', 'Allergy', 'Family Medicine', 
    'Plastic Surgery', 'General Surgery', 'Cardiovascular Surgery', 'Thoracic Surgery', 'Pediatric Surgery', 
    'Neurosurgery', 'Obstetrics and Gynecology', 'Maxillofacial Surgery', 'Vascular Surgery', 'Bariatric Surgery', 
    'Endoscopic Surgery', 'Orthopedic Surgery', 'Oncological Surgery', 'Spinal Surgery', 'Plastic and Reconstructive Surgery'
  ];
  selectedSpecialization: string = '';
  specializationDetails: string = '';
  loading: boolean = false; // Flag for loading animation

  constructor(private http: HttpClient) { }

  ngOnInit(): void {}

  filterBySpecialization(event: Event): void {
    const selectElement = event.target as HTMLSelectElement;
    this.selectedSpecialization = selectElement.value;
    this.fetchSpecializationDetails(this.selectedSpecialization);
  }

  fetchSpecializationDetails(specialization: string): void {
    if (!specialization) {
      this.specializationDetails = 'Please select a specialization to see the details.';
      return;
    }

    this.specializationDetails = ''; // Clear previous details
    this.loading = true; // Start loading animation

    const apiUrl = `http://localhost:5210/api/MedicalSpecialization/${specialization}`;
    this.http.get<{ specialization: string; description: string }>(apiUrl).subscribe({
      next: (response) => {
        this.specializationDetails = response.description; // Extract and display only the description
        this.loading = false; // Stop loading animation
      },
      error: (error) => {
        console.error('Error fetching specialization details:', error);
        this.specializationDetails = 'Failed to fetch specialization details. Please try again later.';
        this.loading = false; // Stop loading animation
      }
    });
  }
}