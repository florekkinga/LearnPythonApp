from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock


class RootWidget(FloatLayout):
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
            self.ids.points.text = "POINTS: {}".format(self.ppp)
        elif self.ids.video.source == "wstawianie.gif" and self.answer == "C":
            self.ppp = self.ppp + 1
            self.ids.points.text = "POINTS: {}".format(self.ppp)
        elif self.ids.video.source == "bubble_sort.gif" and self.answer == "A":
            self.ppp = self.ppp + 1
            self.ids.points.text = "POINTS: {}".format(self.ppp)

        self.ids.answerA.active = False
        self.ids.answerB.active = False
        self.ids.answerC.active = False


class MainApp(App):

    seconds = 30
    widget = None

    def build(self):
        self.widget = RootWidget()
        Clock.schedule_interval(self.Callback_Clock, 1)
        return self.widget

    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.widget.__self__.ids.time.text = "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.widget.__self__.ids.time.text = "FINISH"
            self.seconds = 30
            self.widget.__self__.ids.confirm.trigger_action(duration=0.1)
        if self.widget.__self__.ids.confirm.state == "down":
            self.seconds = 30


if __name__ == '__main__':
    MainApp().run()
