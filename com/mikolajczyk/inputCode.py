from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

from past.builtins import execfile


class RootWidget(FloatLayout):
    key = ObjectProperty(None)
    ppp = 0
    start = 0

    def checkAnswer(self, btn):
        activate_this_file = '/home/radoslaw/PycharmProjects/LearnPythonApp/venv/bin/activate_this.py'
        execfile(activate_this_file, dict(__file__=activate_this_file))
        e = "global factorial"
        e += self.ids.key.text
        e += "\n\n\na = factorial(5)\nout=open('test.txt', 'w')\nout.write(str(a))\nout.close()"
        exec(e)

        file = open("test.txt", "r")
        a = int(file.readline())
        file.close()

        if a == 120:
            self.ppp += 1

            self.ids.points.text = "POINTS: {}".format(self.ppp)
            self.ids.info.text = "ZADANIE: \nBRAWO!"

        else:
            self.ids.info.text = "ZADANIE: \nCOS POSZLO NIE TAK"


class InputApp(App):
    seconds = 60
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
            self.seconds = 60
            self.widget.__self__.ids.confirm.trigger_action(duration=0.1)
        if self.widget.__self__.ids.confirm.state == "down":
            self.seconds = 60


if __name__ == '__main__':
    InputApp().run()
