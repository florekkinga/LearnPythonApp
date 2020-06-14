import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
import points

class SummaryWindow(Screen):
    def start(self):
        if points.globalPoint > 4:
            self.imID.source = "pythonHappy.png"
        else:
            self.imID.source = "pythonSad.png"
        self.txtID.text = "Twój wynik " + str(points.globalPoint)
