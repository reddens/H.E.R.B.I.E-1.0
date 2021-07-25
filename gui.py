import wolfram
import interface
import time
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from voxpopuli import Voice
#voice = Voice(lang="us", pitch=70, speed=120, voice_id=1)
Builder.load_file('my.kv')

class MyGridLayout(Widget):
        def press(self):
            self.ids.buttonimg.source = "alter.png"
            self.ids.picture.source = "thinking.gif"
        def release(self):
            self.ids.buttonimg.source = "send.png"
            query = self.ids.name_input.text
            answer = interface.respond(query.lower())
            #update label 
            self.ids.name_label.text = "You: "+ query + "\n" + "H.E.R.B.I.E: " + str(answer)
            self.ids.picture.source = "herb.gif"
            #voice.say(answer)
            self.ids.name_input.text = ''
        def listen(self):
            self.ids.picture.source = "listening.gif"
            query = interface.record()
            print(query)
            if query == None:
                self.ids.name_label.text = "H.E.R.B.I.E: Sorry, I didn't get that..."
                #voice.say("Sorry, I didn't get that") 
            else:
                answer = interface.respond(query)
                self.ids.name_label.text = "You: "+ str(query) + "\n" + "H.E.R.B.I.E: " + str(answer)
                #voice.say(answer)
        def speak(self):
            interface.playsound("beep.wav")
            self.listen()
            self.ids.picture.source = "herb.gif"
        def change(self):
            self.ids.picture.source = "listening.gif"
class HERBIEApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    HERBIEApp().run()