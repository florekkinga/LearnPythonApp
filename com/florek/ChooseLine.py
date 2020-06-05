from kivy.uix.boxlayout import BoxLayout


class ChooseLine(BoxLayout):
    points = 0
    answer = ""
    correct_answer = "C"

    def checkAnswer(self):

        if self.answer == self.correct_answer:
            self.points += 1
            self.ids.points.text = "TWOJE PUNKTY:\n" + str(self.points)
