import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import pyaudio

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#text to speech

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#to convert voice into text

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing...")
        query=r.recognizer_google(audio, language="en-in")
        print(f"user said: {query}\n")
        print(query)

    except Exception as e:
        print("say that again pleasee...")
        return "none"

    return query

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("how can i help you !")

if __name__=="__main__":
    speak("I am lily \n Bablu created me.\n  I would like to thank him")
    wishme()
    while True :
        query=takecommand().lower()

    if "notepad" in query:
        os.startfile("C:\\WINDOWS\\system32")
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
    elif "wikipedia" in query:
        speak("searching wikipedia...")
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

    elif "play the song" and "play the music" in query:
        music_dir=("C:\\Users\\BABLU KUMAR")
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[1]))
    elif "the time " in query:
        strtime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is{strtime}")