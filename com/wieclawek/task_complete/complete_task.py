from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock


class rootWidget(FloatLayout):
    answer = "def sort(array=[12,4,5,6,7,3,1,15]):\n    less = []\n    equal = []\n    greater = []\n    if len(array) > 1:\n        pivot = array[0]\n        for x in array:\n            if x < pivot:\n                less.append(x)\n            elif x == pivot:\n                equal.append(x)\n            elif x > pivot:\n                greater.append(x)\n        return sort(less)+equal+sort(greater)\n    else:\n        return array\n"
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


class Main2App(App):

    seconds = 30
    widget = None

    def build(self):
        print("Start")
        self.widget = rootWidget()
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
    Main2App().run()