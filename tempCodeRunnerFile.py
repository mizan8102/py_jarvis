import pyttsx4
import speech_recognition as sr


engine = pyttsx4.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id) # voices[0].id voice setup 

def speak(audio):
  engine.say(audio)
  print(audio)
  engine.runAndWait()
  
def takecommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listing....")
    r.pause_threshold = 1
    audio = r.listen(source, timeout=1, phrase_time_limit=5)
  try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said: {query}")
  
  except Exception as e:
    speak("Say that again please ...")
    return "none"
  return query
  
if __name__ == "__main__":
  takecommand()
    # speak("hello")
