import speech_recognition as sr

import speech_recognition as sr
import time

def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")

        # adjust mic noise level (important)
        r.adjust_for_ambient_noise(source, duration=0.8)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        except sr.WaitTimeoutError:
            print("❗ No speech detected...")
            return None
        except Exception as e:
            print("❗ Mic Error:", e)
            return None

    try:
        print("📝 Recognizing...")
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        return text

    except sr.UnknownValueError:
        print("❗ Could not understand audio")
        return None
    except sr.RequestError as e:
        print("❗ Speech service error:", e)
        return None


# speech_to_text() working fine 