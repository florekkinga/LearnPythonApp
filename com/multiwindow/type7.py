from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import points

class Type7Window(Screen):
    seconds = 30
    widget = None
    answer = "3,1,5,2,6,4,8,9,7,12,10,11,13,15,14,16"
    global ppp
    ppp = 0
    start = 0

    def build(self):
        Clock.schedule_interval(self.Callback_Clock, 1)

    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.time.text = "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.time.text = "FINISH"
            self.seconds = 30
            self.confirm.trigger_action(duration=0.1)
        if self.confirm.state == "down":
            self.seconds = 30

    def checkAnswer(self):
        input = self.input.text

        if (input == self.answer):
            global ppp
            ppp += 1
            points.globalPoint += 1
