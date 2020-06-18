
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
        #pytanie= 'Jaki będzie wynik wywołania max("please help ')?'
        odpowiedzi=['s', ' <- spacja', 'e', 'p', 'Funkcja max zwraca maksymalny, czyli ostatni element napisu', 'Funkcja max zwraca maksymalny element napisu, czyli taki o najwyższej wartości']

    def check(self):
        if(self.cb1.active and self.cb6.active):
            points.globalPoint += 2