from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import random
from com.multiwindow import type1, type2, type3, type4, type5, type6, type7, type8, summary

#Window.clearcolor = (1, 1, 1, 1)
Window.clearcolor = (210 / 255, 243 / 255, 236 / 255, 1)

class MainWindow(Screen):
    pass


class LevelsWindow(Screen):
    pass

class Home(Screen):
    pass


class Kariera(Screen):
    pass


class Nauka(Screen):
    pass


class Powtorka(Screen):
    pass


class Ranking(Screen):
    pass


class MojeKonto(Screen):
    pass


class Easy(Screen):
    pass


class Medium(Screen):
    pass


class Hard(Screen):
    pass


class ImageButton(ButtonBehavior, Image):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my1.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
