import mysql.connector
import pyttsx3
from textextract import extracted_keywords  # Your extracted keywords

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# Typo corrections
typo_corrections = {'nitrate': 'nitrite', 'colour': 'color'}

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nabeel174",
        database="healthcare_chatbot"
    )
    cursor = conn.cursor(dictionary=True)
except mysql.connector.Error as err:
    error_text = f"Database connection error. Please try again later. Details: {err}"
    print(error_text)
    engine.say(error_text)
    engine.runAndWait()
    exit()

# Column mapping: keyword -> (table_name, column_name)
column_mapping = {
    # Patient_records1
    'age': ('Patient_records1', 'Age'),
    'blood group': ('Patient_records1', 'Blood_Group'),
    'blood': ('Patient_records1', 'Blood_Group'),
    'group': ('Patient_records1', 'Blood_Group'),
    'dob': ('Patient_records1', 'DOB'),
    'date of birth': ('Patient_records1', 'DOB'),
    'address': ('Patient_records1', 'Address'),
    'last visit': ('Patient_records1', 'Last_Visit'),
    'next of kin': ('Patient_records1', 'Next_of_kin'),
    'contact number': ('Patient_records1', 'Contact_Number'),
    'medication': ('Patient_records1', 'Medication'),
    # Past_records1
    'past records': ('past_records1', 'Past_Records'),
    'disease': ('past_records1', 'Disease'),
    'date of hospitalisation': ('past_records1', 'Date_of_hospitalisation'),
    'doctor': ('past_records1', 'Doctor'),
    'action taken': ('past_records1', 'Action_Taken'),
    # Biopsy_reports
    'report id': ('Biopsy_reports', 'ReportID'),
    'specimen type': ('Biopsy_reports', 'Specimen_Type'),
    'diagnosis': ('Biopsy_reports', 'Diagnosis'),
    'pathologist name': ('Biopsy_reports', 'Pathologist_Name'),
    'comments': ('Biopsy_reports', 'Comments'),
    'microscopic findings': ('Biopsy_reports', 'Microscopic_Findings'),
    'gross description': ('Biopsy_reports', 'Gross_Description'),
    'clinical history': ('Biopsy_reports', 'Clinical_History'),
    'special stains': ('Biopsy_reports', 'Special_Stains'),
    # Blood_Samples
    'collection date': ('Blood_Samples', 'Collection_Date'),
    'tube type': ('Blood_Samples', 'Tube_Type'),
    'storage temperature': ('Blood_Samples', 'Storage_Temperature'),
    'notes': ('Blood_Samples', 'Notes'),
    # Urinalysis_Report
    'color': ('Urinalysis_Report', 'Color'),
    'appearance': ('Urinalysis_Report', 'Appearance'),
    'specific gravity': ('Urinalysis_Report', 'Specific_Gravity'),
    'ph': ('Urinalysis_Report', 'pH'),
    'protein': ('Urinalysis_Report', 'Protein'),
    'glucose': ('Urinalysis_Report', 'Glucose'),
    'ketones': ('Urinalysis_Report', 'Ketones'),
    'bilirubin': ('Urinalysis_Report', 'Bilirubin'),
    'urobilinogen': ('Urinalysis_Report', 'Urobilinogen'),
    'nitrite': ('Urinalysis_Report', 'Nitrite'),
    'leukocytes': ('Urinalysis_Report', 'Leukocytes'),
    'red blood cells': ('Urinalysis_Report', 'RBCs'),
    'white blood cells': ('Urinalysis_Report', 'WBCs'),
    'epithelial cells': ('Urinalysis_Report', 'Epithelial_Cells'),
    'bacteria': ('Urinalysis_Report', 'Bacteria'),
    'crystals': ('Urinalysis_Report', 'Crystals'),
    'casts': ('Urinalysis_Report', 'Casts')
}

# Ensure patient ID and details exist
if len(extracted_keywords) < 2:
    error_text = "Please provide a valid patient ID and at least one detail to fetch."
    print(error_text)
    engine.say(error_text)
    engine.runAndWait()
    cursor.close()
    conn.close()
    exit()

patient_id = extracted_keywords[0]
# Correct typos in keywords
corrected_keywords = [typo_corrections.get(k.lower(), k.lower()) for k in extracted_keywords[1:]]
keywords_str = " ".join(corrected_keywords)

queried_phrases = set()
full_response = []

# Match longest phrases first
for phrase in sorted(column_mapping.keys(), key=lambda x: -len(x)):
    if phrase in keywords_str and phrase not in queried_phrases:
        queried_phrases.add(phrase)
        table_name, db_column = column_mapping[phrase]

        query = f"SELECT {db_column} FROM {table_name} WHERE PatientID = %s"
        try:
            cursor.execute(query, (patient_id,))
            result = cursor.fetchone()
            if result and result[db_column] is not None:
                full_response.append(f"The {phrase} for patient {patient_id} is: {result[db_column]}")
            else:
                full_response.append(f"No data found for patient {patient_id} for '{phrase}'.")
        except mysql.connector.Error as err:
            full_response.append(f"Database error for '{phrase}'. Please try again later.")

# If nothing was found, give a special audio message
if not full_response:
    full_response.append("Sorry, I could not retrieve any data. Please check the patient ID and keywords.")

# Speak all responses
final_response_text = " ".join(full_response)
print(final_response_text)
engine.say(final_response_text)

# Continuation prompt
continuation_text = "Do you want to check another detail for this patient or a different patient?"
print(continuation_text)
engine.say(continuation_text)

engine.runAndWait()

cursor.close()
conn.close()
