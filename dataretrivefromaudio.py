

import pyttsx3
from textextract import extracted_keywords

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

text_to_speak = " ".join(extracted_keywords)
engine.say(text_to_speak)

engine.runAndWait()
# This is a conceptual example based on the provided files
import mysql.connector

# Establish database connection (as seen in dataretrivefromaudio.py)
conn = mysql.connector.connect(host="Localhost", user="root", password="Nabeel174", database="healthcare_chatbot")
cursor = conn.cursor()
cursor.execute("USE healthcare_chatbot;")
conn.commit()

# Get the patient ID and requested detail from the extracted_keywords list
# Assuming the first keyword is the patient ID and the second is the requested detail
if len(extracted_keywords) >= 2:
    patient_id = extracted_keywords[0]
    requested_detail = extracted_keywords[1]
    
    # Construct a SQL query to retrieve the specific detail for the patient ID
    # This is a simplified example; actual implementation would be more robust
    query = f"SELECT {requested_detail} FROM Patient_records WHERE patientID = {patient_id}"

    try:
        cursor.execute(query)
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
