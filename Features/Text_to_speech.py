import os
import pyttsx3

import pyttsx3

def text_to_speech(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("TTS Error:", e)

# text_to_speech("Hlo my name is thasin khan") working fine 
