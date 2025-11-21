import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def text_to_speech(text):
    print("🤖 Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
    

# text_to_speech("Hlo my name is thasin khan") working fine 
