from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import random
import type1, type2

Window.clearcolor = (1, 1, 1, 1)


class MainWindow(Screen):
    pass


class LevelsWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my1.kv")

class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
