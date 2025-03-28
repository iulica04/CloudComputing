import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { PatientListComponent } from './components/patient-list/patient-list.component';
import { PatientCreateComponent } from './components/patient-create/patient-create.component';
import { PatientUpdateComponent } from './components/patient-update/patient-update.component';
import { PatientDetailComponent } from './components/patient-detail/patient-detail.component';
import { MedicListComponent } from './components/medic-list/medic-list.component';
import { MedicCreateComponent } from './components/medic-create/medic-create.component';
import { MedicUpdateComponent } from './components/medic-update/medic-update.component';
import { MedicGetAllComponent } from './components/medic-get-all/medic-get-all.component';
import { LoginComponent } from './components/login/login.component';
import { SpecializationsComponent } from './components/specializations/specializations.component';
import { ForgotPasswordComponent } from './components/forgot-password/forgot-password.component';
import { ResetPasswordComponent } from './components/reset-password/reset-password.component';
import { MedicDetailComponent } from './components/medic-detail/medic-detail.component';
import { RoleSelectionComponent } from './components/register/role-selection.component';
import { CreateConsultationComponent } from './components/create-consultation/create-consultation.component';
import { UpdateConsultationComponent } from './components/update-consultation/update-consultation.component';
import { MedicalConditionForPatientComponent } from './components/medical-condition-for-patient/medical-condition-for-patient.component';


export const appRoutes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'patients', component: PatientListComponent },
    { path: 'patients/register', component: PatientCreateComponent },
    { path: 'medics/register', component: MedicCreateComponent },
    { path: 'patients/update/:id', component: PatientUpdateComponent },
    { path: 'patients/:id', component: PatientDetailComponent },
    { path: 'medics', component: MedicListComponent },
    { path: 'medics/create', component: MedicCreateComponent },
    { path: 'medics/paginated', component: MedicGetAllComponent },
    { path: 'medics/:id', component: MedicDetailComponent },
    { path: 'medics/update/:id', component: MedicUpdateComponent },
    { path: 'login', component: LoginComponent },
    { path: 'specialties', component: SpecializationsComponent },
    { path: 'forgot-password', component: ForgotPasswordComponent },
    { path: 'reset-password/:token', component: ResetPasswordComponent },
    { path : 'register', component: RoleSelectionComponent },
    { path: 'consultations', component: CreateConsultationComponent },
    { path: 'consultations/update/:id', component: UpdateConsultationComponent},
    { path: 'medical-condition/:id', component: MedicalConditionForPatientComponent }

];

