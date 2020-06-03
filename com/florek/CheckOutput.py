from kivy.uix.boxlayout import BoxLayout

class CheckOutput(BoxLayout):
    points = 0
    answer = ""
    correct_answer = "5\n[1,2,3,4,[5,6,7,8]]"

    def checkAnswer(self):
        self.answer = self.ids.input.text

        if(self.answer == self.correct_answer):
            self.points += 1
            self.ids.points.text = "TWOJE PUNKTY: " + str(self.points)