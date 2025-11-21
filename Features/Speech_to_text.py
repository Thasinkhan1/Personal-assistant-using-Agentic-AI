import speech_recognition as sr

def speech_to_text():
    r = sr.Recognizer()
    print(r)
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("📝 Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("You said:", query)
        return query.lower()

    except Exception as e:
        print("❗ Error:", e)
        return ""

# speech_to_text() working fine 