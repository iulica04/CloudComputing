import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MedicalConditionForPatientComponent } from './medical-condition-for-patient.component';

describe('MedicalConditionForPatientComponent', () => {
  let component: MedicalConditionForPatientComponent;
  let fixture: ComponentFixture<MedicalConditionForPatientComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MedicalConditionForPatientComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MedicalConditionForPatientComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
