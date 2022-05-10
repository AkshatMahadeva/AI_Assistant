import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 220)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as error:
        return "None"

    return query.lower()
