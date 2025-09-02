from speech import audio_to_text

# Dictionary to map number words to digits
number_words_to_digits = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# The number words in your lexicon are no longer needed here as they will be
# converted to digits.
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
    'anesthesiologist', 'patient',
    # Pharmaceuticals and Drugs
    'prescription', 'dose', 'tablet', 'capsule', 'syringe', 'antibiotic',
    'analgesic', 'antacid', 'antidepressant', 'antihistamine', 'vaccine',
    'beta','blockers', 'statins', 'nsaids', 'nonsteroidal anti-inflammatory drugs',
    'diuretics', 'anticoagulants', 'insulin',
    # Database details
    'name', 'date', 'of', 'birth', 'age', 'gender', 'blood', 'group', 'medication', 'last', 'visit', 'next', 'of', 'kin', 'contact', 'number', 'address',
    # Other Key Terms
    'diagnosis', 'prognosis', 'symptom', 'syndrome', 'chronic', 'acute',
    'benign', 'malignant', 'hereditary', 'congenital', 'pathology', 'etiology',
    'blood' ,'pressure', 'heart', 'rate', 'temperature', 'cholesterol', 'glucose',
    'hemoglobin', 'white blood cell count', 'platelets', 'electrolytes',
    'stethoscope', 'sphygmomanometer', 'thermometer', 'crutches', 'wheelchair',
    'defibrillator', 'ventilator', 'scalpel', 'admitted', 'blood', 'oxygen', 'high',

    '10', '11','12','13','14','15','16','17','18'
}

audio_to_text_list = audio_to_text.split()

# Process each word from the speech recognition
processed_keywords = []
for word in audio_to_text_list:
    # Convert number words to digits first
    if word.lower() in number_words_to_digits:
        processed_keywords.append(number_words_to_digits[word.lower()])
    else:
        # Check if the word is in the medical lexicon
        if word.lower() in medical_lexicon:
            processed_keywords.append(word.lower())

# Now `extracted_keywords` will have both converted numbers and filtered keywords
extracted_keywords = processed_keywords

print("Extracted keywords:", extracted_keywords)