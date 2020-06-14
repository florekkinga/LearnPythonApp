import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import points

kivy.require("1.11.1")

class Type4Window(Screen):

    seconds = 30


    # self.widget = CheckOutput()
    def start(self):
        Clock.schedule_interval(self.Callback_Clock, 1)
        # return self.widget
    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.time.text = "POZOSTAŁY CZAS: \n" + "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.time.text = "FINISH"
            self.seconds = 30


    points = 0
    answer = ""
    correct_answer = "C"

    def checkAnswer(self):

        if self.answer == self.correct_answer:
            # self.points += 1
            points.globalPoint += 1
            # self.ids.points.text = "TWOJE PUNKTY:\n" + str(self.points)
