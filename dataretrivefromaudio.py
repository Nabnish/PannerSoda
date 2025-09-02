import mysql.connector
import pyttsx3
from textextract import extracted_keywords


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)


conn = mysql.connector.connect(host="Localhost", user="root", password="Nabeel174", database="healthcare_chatbot")
cursor = conn.cursor()


if len(extracted_keywords) >= 2:
    patient_id = extracted_keywords[0]
    requested_detail = extracted_keywords[1]

    
    column_mapping = {
        'age': 'age', 
        'blood_group': 'blood_group',
        'blood': 'blood_group',  
        'group': 'blood_group',  
        'dob': 'DOB',
        'date': 'DOB',  
        'address':'Address',  
        'birth': 'DOB', 
        'date of birth': 'DOB', 
        'date_of_birth': 'DOB', 
        'last_visit': 'last_visit',
        'last': 'last_visit',  
        'visit': 'last_visit', 
        'next_of_kin': 'next_of_kin',
        'next': 'next_of_kin',  
        'kin': 'next_of_kin',   
        'contact_number': 'contact_number',
        'contact': 'contact_number',  
        'number': 'contact_number',   
        'address': 'address',
        'medication': 'medication',
        'medications': 'medication', 

    
    }

    db_column = column_mapping.get(requested_detail)

    if db_column:
        query = f"SELECT {db_column} FROM Patient_records1 WHERE patientID = {patient_id}"

        try:
            cursor.execute(query)
            result = cursor.fetchone()

            if result and result[0]:
                data = result[0]
                for i in column_mapping:
                    if requested_detail == i:
                        requested_detail = column_mapping[i]
                if requested_detail in ['dob']:
                    from datetime import date
                    today = date.today()
                    birth_date = data
                    print(birth_date)
                   
                else:
                    response_text = f"The {requested_detail} for patient {patient_id} is: {data}"
                
                print(response_text)
                engine.say(response_text)
            else:
                response_text = f"No data found for patient ID {patient_id} or column {requested_detail}."
                print(response_text)
                engine.say(response_text)
        except mysql.connector.Error as err:
            response_text = f"Something went wrong with the database query: {err}"
            print(response_text)
            engine.say(response_text)
    else:
        response_text = f"I don't know how to find information for '{requested_detail}'."
        print(response_text)
        engine.say(response_text)
else:
    response_text = "Please provide a valid patient ID and a specific detail to access."
    print(response_text)
    engine.say(response_text)

engine.runAndWait()

cursor.close()
conn.close()

