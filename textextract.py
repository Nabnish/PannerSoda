from speech import audio_to_text

audio_to_text_list = audio_to_text.split()

medical_lexicon = {
    # Symptoms and Conditions
    'hypertension', 'hypotension', 'arrhythmia', 'tachycardia', 'bradycardia', 'stroke', 'aneurysm', 'edema',
    'asthma', 'bronchitis', 'pneumonia', 'influenza', 'apnea', 'gastritis', 'ulcer', 'appendicitis', 'cirrhosis', 'hepatitis', 
    'arthritis', 'fracture', 'sprain', 'strain', 'scoliosis', 'hernia', 'headache', 'migraine', 'seizure',
    'epilepsy', 'dementia', 'alzheimer', 'parkinson', 'concussion', 'diabetes', 'hypoglycemia', 'hyperthyroidism',
    'hypothyroidism', 'fever', 'infection', 'inflammation', 'sepsis', 'bacteria', 'virus', 'fungus', 'parasite', 'measles',
    'mumps', 'rubella', 'depression', 'anxiety', 'schizophrenia', 'bipolar', 'panic', 'attack', 'phobia',
    'obsessive', 'compulsive', 'disorder', 'fatigue', 'nausea', 'vomiting', 'diarrhea', 'constipation', 'dizziness', 'rash', 
    'allergic', 'cancer', 'dehydration', 'malnutrition',
    # Medical Procedures and Treatments
    'biopsy', 'x-ray', 'mri', 'scan', 'ultrasound', 'endoscopy', 'blood', 'test', 'electrocardiogram', 'ecg', 'ekg', 'surgery',
    'incision', 'amputation', 'bypass', 'transplant', 'stitches', 'suture', 'laparoscopy', 'medication', 'therapy', 'chemotherapy',
    'radiation', 'physical therapy', 'rehabilitation', 'dialysis', 'transfusion', 'immunization', 'vaccination',
    # Medical Professionals and Roles
    'cardiologist', 'neurologist', 'oncologist', 'pulmonologist',
    'gastroenterologist', 'dermatologist', 'pediatrician',
    'gynecologist', 'urologist', 'psychiatrist', 'physician', 'doctor',
    'surgeon', 'nurse', 'therapist', 'paramedic', 'pharmacist', 'radiologist',
    'anesthesiologist', 'patient'
    # Pharmaceuticals and Drugs
    'prescription', 'dose', 'tablet', 'capsule', 'syringe', 'antibiotic',
    'analgesic', 'antacid', 'antidepressant', 'antihistamine', 'vaccine',
    'beta','blockers', 'statins', 'nsaids', 'nonsteroidal anti-inflammatory drugs',
    'diuretics', 'anticoagulants', 'insulin',
    # Database details
    'name', 'date', 'of', 'birth', 'age', 'gender', 'blood', 'group', 'medication', 'last', 'visit', 'next', 'of', 'kin', 'contact', 'number', 'address'
    # Other Key Terms
    'diagnosis', 'prognosis', 'symptom', 'syndrome', 'chronic', 'acute',
    'benign', 'malignant', 'hereditary', 'congenital', 'pathology', 'etiology',
    'blood' ,'pressure', 'heart', 'rate', 'temperature', 'cholesterol', 'glucose',
    'hemoglobin', 'white blood cell count', 'platelets', 'electrolytes',
    'stethoscope', 'sphygmomanometer', 'thermometer', 'crutches', 'wheelchair',
    'defibrillator', 'ventilator', 'scalpel', 'admitted', 'blood', 'oxygen', 'high',

    '1', '2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18'
}

extracted_keywords = [word for word in audio_to_text_list if word in medical_lexicon]

print("Extracted keywords:", extracted_keywords)