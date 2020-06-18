
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
        #pytanie= 'Które z wywołań zwróci/zwrócą 4, zakładając że s = {3, 4, 1, 2}?'
        odpowiedzi=['Sum( s )','Len( s )','Max( s )','Four( s )','print( s[1] )','print( s[2] )','High( s )','Size( s )']


    def check(self):
        if(self.cb2.active and self.cb3.active and self.cb5.active):
            points.globalPoint += 2