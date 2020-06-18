
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
        #pytanie= 'Jaki będzie wynik wywołania poniższego kodu?'
        odpowiedzi=['dziesiętnie: 39','dziesiętnie: 40','dziesiętnie: 41','dziesiętnie: 42','binarnie: 100111','binarnie: 101000','binarnie: 101001','binarnie: 101010']
    def check(self):
        if(self.cb4.active and self.cb8.active):
            points.globalPoint += 2