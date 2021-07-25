import speech_recognition as sr 
import pyaudio
r = sr.Recognizer()
mics = sr.Microphone.list_microphone_names()
print(mics)