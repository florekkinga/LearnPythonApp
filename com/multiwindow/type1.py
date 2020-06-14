import random
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
import points

pytania = [
    ["print(int(2.9 + 2))", "4"], ["print(round(15.9) / int(4.9))", "4.0"], ["print(int(1.9) + 2)", "3"], ["print(len(\"aaaaa\"))", "5"], ["print(15//2)", "7"], ["print(17%5)", "2"]
]
buttonsPressed = [
    [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""], [0, ""]
]
red = [255, 255, 0, 1]
green = [0, 255, 255, 1]
blue = [0, 0, 255, 1]
purple = [255, 0, 255, 1]

text = "Dopasuj kod \nz outputem"

count = 0

pyt = []
kol = []
pytOdp = []



class SecondWindow(Screen):

    # def load(self):
    #     buttonsPressed[0][1].disabled = True
    #     buttonsPressed[1][1].disabled = True
    #     buttonsPressed[2][1].disabled = True
    #     buttonsPressed[3][1].disabled = True
    #     buttonsPressed[4][1].disabled = True
    #     buttonsPressed[5][1].disabled = True
    #     buttonsPressed[6][1].disabled = True
    #     buttonsPressed[7][1].disabled = True

    def start(self):

        global kol
        global pyt
        global pytOdp

        self.spr.disabled = False

        pytOdp = []

        self.mt1.text = "Dopasuj kod \nz outputem"

        buttonsPressed[0][1] = self.p1
        buttonsPressed[1][1] = self.p2
        buttonsPressed[2][1] = self.p3
        buttonsPressed[3][1] = self.p4
        buttonsPressed[4][1] = self.o1
        buttonsPressed[5][1] = self.o2
        buttonsPressed[6][1] = self.o3
        buttonsPressed[7][1] = self.o4

        buttonsPressed[0][1].disabled = False
        buttonsPressed[1][1].disabled = False
        buttonsPressed[2][1].disabled = False
        buttonsPressed[3][1].disabled = False
        buttonsPressed[4][1].disabled = True
        buttonsPressed[5][1].disabled = True
        buttonsPressed[6][1].disabled = True
        buttonsPressed[7][1].disabled = True

        pyt = random.sample(range(len(pytania)), 4)
        kol = random.sample(range(4), 4)

        self.p1.text = pytania[pyt[0]][0]
        self.p2.text = pytania[pyt[1]][0]
        self.p3.text = pytania[pyt[2]][0]
        self.p4.text = pytania[pyt[3]][0]

        self.o1.text = pytania[pyt[kol[0]]][1]
        self.o2.text = pytania[pyt[kol[1]]][1]
        self.o3.text = pytania[pyt[kol[2]]][1]
        self.o4.text = pytania[pyt[kol[3]]][1]

        pytOdp = [
            [kol[0], 0], [kol[1], 1], [kol[2], 2], [kol[3], 3]
        ]

        for i in range(len(buttonsPressed)):
            buttonsPressed[i][1].background_color = [1,1,1,1.0]
        global count

        count = 0



    def colorChange(self, inst):
        buttonsPressed[inst][0] = 1

        if inst > -1 and inst <= 3:
            for j in [4,5,6,7]:
                buttonsPressed[j][1].disabled = False
            for i in [0,1,2,3]:
                buttonsPressed[i][1].disabled = True
            for o in range(len(buttonsPressed)):
                if buttonsPressed[o][0] == 1:
                    buttonsPressed[o][1].disabled = True
        else:
            for i in [0,1,2,3]:
                buttonsPressed[i][1].disabled = False
            for j in [4,5,6,7]:
                buttonsPressed[j][1].disabled = True
            for o in range(len(buttonsPressed)):
                if buttonsPressed[o][0] == 1:
                    buttonsPressed[o][1].disabled = True





        global count

        if count < 2:
            buttonsPressed[inst][1].background_color = red
            count = count + 1
        elif count >= 2 and count < 4:
            buttonsPressed[inst][1].background_color = green
            count = count + 1
        elif count >= 4 and count < 6:
            buttonsPressed[inst][1].background_color = blue
            count = count + 1
        elif count >= 6 and count < 8:
            buttonsPressed[inst][1].background_color = purple
            count = count + 1

    def next(self):
        global kol
        global pyt
        global pytOdp
        correct = 0

        if buttonsPressed[pytOdp[0][0]][1].background_color == buttonsPressed[pytOdp[0][1] + 4][1].background_color and buttonsPressed[pytOdp[0][0]][1].background_color != [1,1,1,1.0]:
            correct = correct + 1
        if buttonsPressed[pytOdp[1][0]][1].background_color == buttonsPressed[pytOdp[1][1] + 4][1].background_color and buttonsPressed[pytOdp[1][0]][1].background_color != [1,1,1,1.0]:
            correct = correct + 1
        if buttonsPressed[pytOdp[2][0]][1].background_color == buttonsPressed[pytOdp[2][1] + 4][1].background_color and buttonsPressed[pytOdp[2][0]][1].background_color != [1,1,1,1.0]:
            correct = correct + 1
        if buttonsPressed[pytOdp[3][0]][1].background_color == buttonsPressed[pytOdp[3][1] + 4][1].background_color and buttonsPressed[pytOdp[3][0]][1].background_color != [1,1,1,1.0]:
            correct = correct + 1

        points.globalPoint += correct


        self.mt1.text = str(correct)+"/4pkt"
