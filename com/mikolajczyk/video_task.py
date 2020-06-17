from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock
import random

SECONDS = 30


class RootWidget(FloatLayout):
    video = ObjectProperty(None)
    textA = ObjectProperty(None)
    textB = ObjectProperty(None)
    textC = ObjectProperty(None)
    taskText = ObjectProperty(None)
    points = ObjectProperty(None)
    answer = ''
    ppp = 0
    wasIt = [1, 2, 3, 4, 5, 6]
    file = open("baza_pytan.txt", "r")
    ans = []

    isPressed = False

    def update(self, btn):
        rand = random.randrange(1, 6)
        self.checkCorrectness()
        self.chooseTask(rand)

        self.isPressed = True

        self.ids.answerA.active = False
        self.ids.answerB.active = False
        self.ids.answerC.active = False

    def chooseTask(self, rand):

        if rand == 1 and self.wasIt.__contains__(1):
            self.wasIt.remove(1)
            self.ids.video.source = "bubble_sort.gif"
            self.firstPacket()

        elif rand == 2 and self.wasIt.__contains__(2):
            self.wasIt.remove(2)
            self.ids.video.source = "scalanie.gif"
            self.firstPacket()

        elif rand == 3 and self.wasIt.__contains__(3):
            self.wasIt.remove(3)
            self.ids.video.source = "wstawianie.gif"
            self.firstPacket()

        elif rand == 4 and self.wasIt.__contains__(4):
            self.wasIt.remove(4)
            self.ids.video.source = "prima.gif"
            self.secondPacket()

        elif rand == 5 and self.wasIt.__contains__(5):
            self.wasIt.remove(5)
            self.ids.video.source = "dijkstra.gif"
            self.secondPacket()

        elif rand == 6 and self.wasIt.__contains__(6):
            self.wasIt.remove(6)
            self.ids.video.source = "kruskal.gif"
            self.secondPacket()

        elif len(self.wasIt) == 0:
            App.get_running_app().stop()
            print("Uzyskales: " + str(self.ppp) + " punktow")
        else:
            self.chooseTask(self.wasIt[0])

    def firstPacket(self):
        self.ids.taskText.text = "Zadanie: Na podstawie filmiku wybierz odpowiedź A, B, C. Przedstawiona animacja obrazuje sortowanie:"
        self.ids.textA.text = "Sortowanie bąbelkowe"
        self.ids.textB.text = "Sortowanie przez scalanie"
        self.ids.textC.text = "Sortowanie przez wstawianie"

    def secondPacket(self):
        self.ids.taskText.text = "Zadanie: Na podstawie filmiku wybierz odpowiedź A, B, C. Przedstawiona animacja obrazuje:"
        self.ids.textA.text = "Algorytm Prima"
        self.ids.textB.text = "Algorytm Dijkstry"
        self.ids.textC.text = "Algorytm Kruskala"

    def readFromFile(self):
        for x in self.file:
            b = x.replace("\n", "")
            self.ans.append(b)
        self.file.close()

    def checkCorrectness(self):
        if self.ids.video.source == 'bubble_sort.gif' and self.ans[0] == self.answer:
            self.givePoint()
        elif self.ids.video.source == 'scalanie.gif' and self.ans[1] == self.answer:
            self.givePoint()
        elif self.ids.video.source == 'wstawianie.gif' and self.ans[2] == self.answer:
            self.givePoint()
        elif self.ids.video.source == 'prima.gif' and self.ans[3] == self.answer:
            self.givePoint()
        elif self.ids.video.source == 'dijkstra.gif' and self.ans[4] == self.answer:
            self.givePoint()
        elif self.ids.video.source == 'kruskal.gif' and self.ans[5] == self.answer:
            self.givePoint()

    def givePoint(self):
        self.ppp += 1
        self.ids.points.text = "POINTS: {}".format(self.ppp)


class MainApp(App):
    AMOUNT = SECONDS
    seconds = AMOUNT
    widget = None
    rand = random.randrange(1, 6)

    def build(self):
        self.widget = RootWidget()
        self.widget.readFromFile()
        self.widget.chooseTask(self.rand)
        Clock.schedule_interval(self.Callback_Clock, 1)
        return self.widget

    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.widget.__self__.ids.time.text = "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.widget.__self__.ids.time.text = "FINISH"
            self.seconds = self.AMOUNT
            self.widget.__self__.ids.confirm.trigger_action(duration=0.1)
        if self.widget.__self__.isPressed:
            self.seconds = self.AMOUNT
        self.widget.__self__.isPressed = False


if __name__ == '__main__':
    MainApp().run()
