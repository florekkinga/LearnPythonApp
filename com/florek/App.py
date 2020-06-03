import kivy
from com.florek.CheckOutput import CheckOutput
from kivy.app import App
from kivy.clock import Clock

kivy.require("1.11.1")


# class CheckOutput(BoxLayout):
#     pass

class WdiApp(App):
    seconds = 30

    def build(self):
        self.widget = CheckOutput()
        Clock.schedule_interval(self.Callback_Clock, 1)
        # return ConnectPage()
        return self.widget
        # return ChooseLine()

    def Callback_Clock(self, dt):
        self.seconds = self.seconds - 1
        self.widget.__self__.ids.time.text = "POZOSTAŁY CZAS: \n" + "00:{}".format(self.seconds)
        if self.seconds == 0:
            self.widget.__self__.ids.time.text = "FINISH"
            self.seconds = 30
            self.widget.__self__.ids.confirm.trigger_action(duration=0.1)
        # if self.widget.__self__.ids.confirm.state == "down":
        #     self.seconds = 30

if __name__ == "__main__":
    WdiApp().run()