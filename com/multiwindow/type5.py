import kivy
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import points

class Type5Window(Screen):

    video = ObjectProperty(None)
    answer = ""
    ppp = 0
    start = 0

    def update(self, btn):

        self.start = self.start + 1
        if self.start == 3:
            self.start = 0

        if self.start == 0:
            self.ids.video.source = "bubble_sort.gif"
        elif self.start == 1:
            self.ids.video.source = "scalanie.gif"
        elif self.start == 2:
            self.ids.video.source = "wstawianie.gif"

        if self.ids.video.source == "scalanie.gif" and self.answer == "B":
            self.ppp = self.ppp + 1
            points.globalPoint += 1
            # self.ids.points.text = "POINTS: {}".format(self.ppp)
        elif self.ids.video.source == "wstawianie.gif" and self.answer == "C":
            self.ppp = self.ppp + 1
            points.globalPoint += 1
            # self.ids.points.text = "POINTS: {}".format(self.ppp)
        elif self.ids.video.source == "bubble_sort.gif" and self.answer == "A":
            self.ppp = self.ppp + 1
            points.globalPoint += 1
            # self.ids.points.text = "POINTS: {}".format(self.ppp)

        self.ids.answerA.active = False
        self.ids.answerB.active = False
        self.ids.answerC.active = False

    AMOUNT = 30
    seconds = AMOUNT
    widget = None

    def start1(self):
        Clock.schedule_interval(self.Callback_Clock, 1)

    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.time.text = "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.time.text = "FINISH"
            self.seconds = self.AMOUNT
            self.confirm.trigger_action(duration=0.1)
        if self.confirm.state == "down":
            self.seconds = self.AMOUNT
