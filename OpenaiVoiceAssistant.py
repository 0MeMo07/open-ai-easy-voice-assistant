import openai
import time
import speech_recognition as sr
import pyttsx3
import pyaudio
from ecapture import ecapture as ec

while True:
    engine=pyttsx3.init('sapi5')
    engine.setProperty("rate", 200)
    voices=engine.getProperty('voices')
    engine.setProperty('voice','voices[64].id')
    engine.runAndWait()


    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def takeCommand():
        while True:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source)

            try:
                statement=r.recognize_google(audio,language='en')
                print(f"user said:{statement}\n")

            except Exception as e:
                return "None"
            return statement
        
    def gpt3(stext):
        openai.api_key = "YOUR APİ KEY"

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=stext,
                temperature=0.1,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )
        content = response.choices[0].text.split('.')
        print(content)
        return response.choices[0].text

    statement = takeCommand().lower()


    if "open ai" in statement or "hey open ai" in statement or "hey" in statement:
        speak("Yes im listening")

        statement= takeCommand().lower()

        sorusor = statement
        response = gpt3(sorusor)
        speak(response)