from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class RootWidget(FloatLayout):
    pass


class MainApp(App):
    def build(self):
        widget = RootWidget()

        return widget


if __name__ == '__main__':
    MainApp().run()
