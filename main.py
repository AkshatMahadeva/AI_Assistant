from Speak import speak, takeCommand
import wikipedia
import datetime
import webbrowser
import pyfiglet

starting = pyfiglet.figlet_format('ROBERT THE AI')
print(starting)

assname = ("Robert")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

speak(f"I am {assname} Your personal A.I. assistant")






