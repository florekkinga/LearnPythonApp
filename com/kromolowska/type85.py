
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
        #pytanie= 'Które z nich nie może/mogą być identyfikatorem w Pythonie?'
        odpowiedzi=['1abc','$12','a','_xy1','@ python','aaa','b612','123','pyth','.1']
    def check(self):
        if(self.cb1.active and self.cb2.active and self.cb4.active and self.cb7.active and self.cb8.active):
            points.globalPoint += 2