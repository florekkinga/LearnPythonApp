from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock


class RootWidget(FloatLayout):
    answer = "3,1,5,2,6,4,8,9,7,12,10,11,13,15,14,16"
    ppp = 0
    start = 0

    def checkAnswer(self):
        self.input = self.ids.input.text

        if (self.input == self.correct_answer):
            self.points += 1

            self.ids.points.text = "POINTS: {}".format(self.ppp)

            print("OK")
        else:
            print("Ehh")


class MainApp(App):

    seconds = 5
    widget = None

    def build(self):
        print("Start")
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