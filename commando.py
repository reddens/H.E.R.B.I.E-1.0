import speech_recognition as sr
import webbrowser
import datetime
import subprocess
import interface
import time 
import requests
import cv2
from voxpopuli import Voice

def runCommand(statement):
    if "bye" in statement or "ok bye" in statement or "stop" in statement:
                print('Goodbye')
                return "Goodbye"
                exit()
    elif 'open youtube' in statement:
        webbrowser.open_new_tab("https://www.youtube.com")
        return "Opening Youtube..."
        time.sleep(5)

    elif 'open google' in statement:
        webbrowser.open_new_tab("https://www.google.com")
        return "Opening Google..."
        time.sleep(5)

    elif 'open gmail' in statement:
        webbrowser.open_new_tab("gmail.com")
        return ("Opening Google Mail...")
        time.sleep(5)

    elif 'time' in statement:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        return f"The time is {strTime}"
    elif 'news' in statement:
        news = webbrowser.open_new_tab("https://www.bbc.com/news")
        speak('Here are some headlines from the BBC')
        time.sleep(6)

    elif "camera" in statement or "take a photo" in statement:
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while(result):
            ret,frame = videoCaptureObject.read()
            cv2.imwrite("NewPicture.jpg",frame)
            result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()

    elif 'search'  in statement:
        statement = statement.replace("search", "")
        statement = statement.replace("for", "")
        webbrowser.open_new_tab("https://www.duckduckgo.com/?q="+statement)
        time.sleep(5)	

    elif 'search for' in statement:
        statement = statement.replace("search for", "")
        webbrowser.open_new_tab("https://www.duckduckgo.com/?q="+statement)
        time.sleep(5)


    elif "weather" in statement:
        api_key="Apply your unique ID"
        base_url="https://api.openweathermap.org/data/2.5/weather?"
        speak("what is the city name")
        city_name=interface.record()
        complete_url=base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()
        if x["cod"]!="404":
            y=x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            speak(" Temperature in kelvin unit is " +
                    str(current_temperature) +
                    "\n humidity in percentage is " +
                    str(current_humidiy) +
                    "\n description  " +
                    str(weather_description))
            print(" Temperature in kelvin unit = " +
                    str(current_temperature) +
                    "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                    "\n description = " +
                    str(weather_description))



    elif "shutdown" in statement or "shut down" in statement or "power off" in statement:
        speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
        subprocess.call(["sudo", "init", "0"])
