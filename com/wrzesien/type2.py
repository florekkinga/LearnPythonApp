import random
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen


ran2 = 0

text2 = "Popraw błędy\nw kodzie"

baza = [
    ["def wypiszMax(a, b):\n    if a > b:\n        print(a, 'to maksimum')\n    elif a == b:\n        print(a, 'jest równe', b)\n    else:\n        print(b, 'to maksimum')", "def wypiszMax(a, b):\n    if a > b:\n        print(a, 'to maksimum')\n    elif a = b:\n        print(a, 'jest równe', b)\n    else:\n        printer(b, 'to maksimum')"],
    ["def tri_recursion(k):\n    if(k > 0):\n        result = k + tri_recursion(k - 1)\n        print(result)\n    else:\n         result = 0\n    return result", "def tri_recursion(k):\n    if(k > 0):\n        result = k + tri_recurson(k - 1)\n        print(result)\n    else:\n         result == 0\n    return result"],
    ["class Dog:\n    tricks = []\n    def __init__(self, name):\n        self.name = name\n    def add_trick(self, trick):\n        self.tricks.append(trick)", "class Dog:\n    tricks = []\n    df _init_(self, name):\n        self.name = name\n    df add_trick(self, trick):\n        self.tricks.append(trick)"]
    ]


class Type2Window(Screen):
    def start(self):
        self.mt1.text = text2
        global ran2
        ran2 = random.choice(range(len(baza)))
        self.ti1.text = baza[ran2][1]

    def next(self):
        if self.ti1.text == baza[ran2][0]:
            self.mt1.text = "OK"
        else:
            self.mt1.text = "Nie OK"
