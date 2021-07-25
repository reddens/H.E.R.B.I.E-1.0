import speech_recognition as sr 
r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    statement = r.listen(source)
    msg = r.recognize_google(statement)

print("You: "+ msg)