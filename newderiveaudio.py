import pyttsx3
# The imported list is already processed and contains digits
from textextract import extracted_keywords
import mysql.connector

# Use the already processed list for both TTS and database access
text_to_speak = " ".join(extracted_keywords)
print("Text to speak:", text_to_speak)

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

engine.say(text_to_speak)
engine.runAndWait()

# This is a conceptual example based on the provided files
# Establish database connection (as seen in dataretrivefromaudio.py)
conn = mysql.connector.connect(host="Localhost", user="root", password="Nabeel174", database="healthcare_chatbot")
cursor = conn.cursor()
cursor.execute("USE healthcare_chatbot;")
conn.commit()

# Get the patient ID and requested detail from the processed_keywords list
if len(extracted_keywords) >= 2:
    # The first element is now a digit string
    patient_id = extracted_keywords[0]
    requested_detail = extracted_keywords[1]
    
    # Construct a SQL query to retrieve the specific detail for the patient ID
    # This is a simplified example; actual implementation would be more robust
    query = f"SELECT {requested_detail} FROM Patient_records WHERE patientID = %s"

    try:
        cursor.execute(query, (patient_id,))
        result = cursor.fetchone()
        if result:
            print(f"The {requested_detail} for patient_records {patient_id} is: {result[0]}")
        else:
            print(f"No data found for patient ID {patient_id}.")
    except mysql.connector.Error as err:
        print(f"Something went wrong: {err}")

# Close the connection
cursor.close()
conn.close()