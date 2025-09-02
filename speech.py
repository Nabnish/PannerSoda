import speech_recognition as sr
import time

# Grab user speech
user_speech_recognizer= sr.Recognizer()

with sr.Microphone() as user_audio_source:
    print("Start speaking")
    print("Format: [Patient ID] [Relevant details to be accessed (e.g. blood group, next of kin, address, medication)]")
    user_speech_recognizer.adjust_for_ambient_noise(user_audio_source)
    user_audio = user_speech_recognizer.listen(user_audio_source, phrase_time_limit=20)

try:
    audio_to_text = user_speech_recognizer.recognize_google(user_audio, language='en-US')
    print("User: " + audio_to_text)
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

