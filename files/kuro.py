#libraries
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
from jokes import jokes  # Import the jokes list from jokes.py

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, sire")

    elif 12 <= hour < 18:
        speak("Good Afternoon, Sama!")

    elif 18 <= hour < 21:
        speak("Good Evening, Sama!")

    else:
        speak("Good Night, Sama!")

    speak("I'm Kuro. How can I help you?")

def tellJoke():
    joke = random.choice(jokes)
    speak(joke)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again, please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()  # Wishing you at startup
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("I found multiple results. Please specify your query.")
            except wikipedia.exceptions.PageError as e:
                speak("Sorry, I couldn't find any information on that topic.")
                
        elif 'open youtube' in query:
            webbrowser.open_new_tab('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open_new_tab('https://www.google.com')

        elif 'tell me a joke' in query:
            tellJoke()
