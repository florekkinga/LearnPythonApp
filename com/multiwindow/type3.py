import random
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import points

Window.clearcolor = (1, 1, 1, 1)
ran = 0
pressedButton = [[0, ""], [0,""]]
baseTrueFalse = [["Do wczytania danych z klawiatury\nsłuży funkcja output()", False],
                 ["Aby połączyć wyrażenia warunkowe \nw Pythonie należy użyć znaków &&", False],
                 ["W języku Python definicja funkcji \npowinna zaczynać się od 'def'", True],
                 ["W języku Python do mnożenia \nużywamy operatora **", False],
                 ["W Pythonie linię możemy \nzakomentować znakiem %", False],
                 ["Python nie jest językiem \niterpretowanym", False],
                 ["W metodach klasy używamy \nargumentu 'self'", True],
                 ["Do wykonania operacji modulo \nużywamy operatora '%'", True],
                 ["Typ zmiennej w Pythonie, która przyjmuje \nwartości 'True' lub 'False' to bool", False],
                 ["W Pythonie nie jest możliwe stworzenie \nfunkcji o zmiennej liczbie argumentów", False]
                 ]

class Type3Window(Screen):
    def start(self):
        global ran
        global pressedButton
        pressedButton[0][1] = self.bt
        pressedButton[1][1] = self.bf

        ran = random.choice(range(len(baseTrueFalse)))
        self.question.text = baseTrueFalse[ran][0]

    def check(self, instance):
        global ran
        if (instance == True and baseTrueFalse[ran][1] == True) or (instance == False and baseTrueFalse[ran][1] == False):
            self.text.text = "Wybrałeś dobrze"
            points.globalPoint += 1
        else:
            self.text.text = "Wybrałeś źle"
