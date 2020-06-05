#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random


Window.clearcolor = (1, 1, 1, 1)
ran = 0
pressedButton = [[0, ""], [0,""]]
baseTrueFalse = [["Do wczytania danych z klawiatury służy funkcja output()", False],
                 ["Aby połączyć wyrażenia warunkowe w Pythonie należy użyć znaków &&", False],
                 ["W języku Python definicja funkcji powinna zaczynać się od 'def'", True],
                 ["W języku Python do mnożenia używamy operatora **", True],
                 ["W Pythonie linię możemy zakomentować znakiem %", False],
                 ["Python nie jest językiem iterpretowanym", False],
                 ["W metodach klasy używamy argumentu 'self'", True],
                 ["Do wykonania operacji modulo używamy operatora '%'", True],
                 ["Typ zmiennej w Pythonie, która przyjmuje wartości 'True' lub 'False' to bool", False],
                 ["W Pythonie nie jest możliwe stworzenie funkcji o zmiennej liczbie argumentów", False]
                 ]

class TrueFalseApp(App):
    def build(self):
        return MyLayout()


class MyLayout(Widget):
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
        else:
            self.text.text = "Wybrałeś źle"


if __name__ == "__main__":
    TrueFalseApp().run()
