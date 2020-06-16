import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.config import Config

Window.clearcolor = (210 / 255, 243 / 255, 236 / 255, 1)
# Window.size = (800, 600)
kivy.require("1.11.1")


class Home(Screen):
    pass


class SzybkaGra(Screen):
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


class WindowManager(ScreenManager):
    pass


class ImageButton(ButtonBehavior, Image):
    pass


kv = Builder.load_file("nice.kv")


class NiceApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    NiceApp().run()
