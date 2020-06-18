import random
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import points

Window.clearcolor = (1, 1, 1, 1)
ran = 0
pressedButton = [[0, ""], [0,""]]
#baseTrueFalse = [["Do wczytania danych z klawiatury\nsłuży funkcja output()", False],
#                 ["Aby połączyć wyrażenia warunkowe \nw Pythonie należy użyć znaków &&", False],
#                 ["W języku Python definicja funkcji \npowinna zaczynać się od 'def'", True],
#                 ["W języku Python do mnożenia \nużywamy operatora **", False],
#                 ["W Pythonie linię możemy \nzakomentować znakiem %", False],
#                ["Python nie jest językiem \niterpretowanym", False],
#                  ["W metodach klasy używamy \nargumentu 'self'", True],
#                  ["Do wykonania operacji modulo \nużywamy operatora '%'", True],
#                  ["Typ zmiennej w Pythonie, która przyjmuje \nwartości 'True' lub 'False' to bool", False],
#                  ["W Pythonie nie jest możliwe stworzenie \nfunkcji o zmiennej liczbie argumentów", False]
#                  ]

file = open("bazaTrueFalse.txt", "r")
base = []
for line in file:
        x=line.replace("\r", "")
        x=line.replace("\n", "")
        x=line.split(";")
        base.append(x)

class Type3Window(Screen):
    def start(self):
        global ran
        global pressedButton
        pressedButton[0][1] = self.bt
        pressedButton[1][1] = self.bf

        ran = random.choice(range(len(base)))
        self.question.text = base[ran][0]

    def check(self, instance):
        global ran
        if (instance == True and base[ran][1] == "True\n") or (instance == False and base[ran][1] == "False\n"):
            self.text.text = "Wybrałeś dobrze"
            points.globalPoint += 1
        else:
            self.text.text = "Wybrałeś źle"
