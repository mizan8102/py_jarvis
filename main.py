import pyttsx4
import speech_recognition as sr

engine = pyttsx4.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to 'voice' instead of 'voices'

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:  # Change the device_index if needed
        print("Listening...")
        r.pause_threshold = 1.5  # Increase the pause_threshold value
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query

    except Exception as e:
        speak("Say that again please...")
        return "none"

if __name__ == "__main__":
    sp=takecommand()
    speak(sp)
