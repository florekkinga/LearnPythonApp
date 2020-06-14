from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import points

class Type6Window(Screen):
    points = 0
    answer = ""
    seconds = 30
    correct_answer = "5\n[1,2,3,4,[5,6,7,8]]"


    def start(self):
        Clock.schedule_interval(self.Callback_Clock, 1)
        # return self.widget
    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.time.text = "POZOSTAŁY CZAS: \n" + "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.time.text = "FINISH"
            self.seconds = 30

    def checkAnswer(self):
        self.answer = self.ids.input.text

        if self.answer == self.correct_answer:
            self.points += 1
            # self.ids.points.text = "TWOJE PUNKTY:\n" + str(self.points)
            points.globalPoint += 1
