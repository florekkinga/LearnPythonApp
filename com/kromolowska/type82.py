
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import points

class Type8Window(Screen):
    def build(self):
        #pytanie= 'Które zdanie/zdania jest/są prawdziwe i dotyczą rekurencji?'
        odpowiedzi=['Są znacznie szybsze niż normalne funkcje.','Zajmują więcej miejsca niż funkcje nierekurencyjne.','Zawsze można je zastąpić funkcjami nierekurencyjnymi.','Korzystanie z funkcji rekurencyjnych daje jednak naturalne i proste proste rozwiązanie dla programu.']

    def check(self):
        if(self.cb2.active and self.cb3.active and self.cb4.active):
            points.globalPoint += 2