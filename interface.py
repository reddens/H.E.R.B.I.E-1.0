import datetime
from os import stat
import speech_recognition as sr
import wolfram
import commando
import bot
import taske
from playsound import playsound
r = sr.Recognizer()
#Interface
question_regex = []

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return("Good Morning")
    elif hour >= 12 and hour < 18:
        return("Good Afternoon")
    else:
        return("Good Evening")

def record():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            msg = r.recognize_google(audio, language='en')
            print("You: "+msg)
            return str(msg)
        except Exception as e:
            print("ERROR")
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en')
            if "Herbie" in str(statement):
                playsound("beep.wav")
                return True
        except Exception as e:
            return None


def respond(query):
    command = ''
    question = ''
    chat = ''
    if "news" in query or "gmail" in query or "calendar" in query or "schedule" in query or "time" in query or "to do" in query or "twitter" in query or "open" in query or "Open" in query:
         print("command detected")
         command = True
    elif "who" in query or "where" in query or "when" in query or "what" in query or "how" in query or "which" in query or "why" in query or "did" in query or "is" in query:
         print("question detected")
         question = True
    else:
         chat = True

    if chat == True:
        response = bot.respond(query)
    elif question == True:
        response = wolfram.search(query)
    elif command == True:
        response = commando.runCommand(query)
    else:
        print("I don't understand")
    return response
