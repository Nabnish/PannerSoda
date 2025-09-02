import pyttsx3
from textextract import extracted_keywords

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9) # Volume (0.0 to 1.0)

text_to_speak = " ".join(extracted_keywords)
engine.say(text_to_speak)

engine.runAndWait()