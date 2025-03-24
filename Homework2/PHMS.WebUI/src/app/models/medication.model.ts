export interface Medication {
    id: string;
    treatmentId: string; 
    name: string;
    type: MedicationType;
    dosage: string;
    administration: string;
    ingredients: string;
    adverseEffects: string;
  }
  
  export enum MedicationType {
    Tablet,
Capsule,
Syrup,
Injection,
Cream,
Ointment,
Drops,
Inhaler,
Spray,
Patch,
Suppository,
Implant,
Powder,
Gel,
Lotion,
Liquid,
Lozenge,
Solution,
Suspension,
Syringe,
Analgesic,
NSAID,
Antibiotic,
Antidiabetic,
ACEInhibitor,
Antihistamine,
Statin,
ProtonPumpInhibitor,
ARB,
Corticosteroid,
Diuretic,
Anticonvulsant,
Benzodiazepine,
SSRI,
Anticoagulant,
H2Blocker,
Antiplatelet,
Opioid,
Hormone,
Other
  }