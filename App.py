import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
kivy.require("1.11.1")

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="TEXT1"))
        self.input1 = TextInput(multiline = True)
        self.add_widget(self.input1)

        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)

        self.add_widget(Label(text="Email"))
        self.email = TextInput(multiline = False)
        self.add_widget(self.email)

        self.add_widget(Label())
        self.join = Button(text="Join")
        self.join.bind(on_press = self.join_button)
        self.add_widget(self.join)

    def join_button(self, instance):
        text1 = self.input1.text
        username = self.username.text
        email = self.email.text
        with open("prev_details.txt","w") as f:
            f.write(f"{text1},{username},{email}")
        print(f"Joining {text1}:{email} as {username}")




class WdiApp(App):
    def build(self):
        return ConnectPage()

if __name__ == "__main__":
    WdiApp().run()