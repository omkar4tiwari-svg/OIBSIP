import speech_recognition as sr
try:
    import pyttsx3
except ImportError:
    # Fallback stub if pyttsx3 is not installed — allows the script to run without TTS
    class _DummyEngine:
        def say(self, text):
            pass
        def runAndWait(self):
            pass
    pyttsx3 = None
import datetime
import webbrowser
import wikipedia

# Text to Speech
if 'pyttsx3' in globals() and pyttsx3:
    engine = pyttsx3.init()
else:
    engine = _DummyEngine()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Take Voice Command
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Sorry, I could not understand.")
        return ""

# Wish User
def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your voice assistant. How can I help you?")

# Main Function
wish()

while True:
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "search" in command:
        speak("What should I search?")
        query = take_command()

        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("No result found.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        break
    