from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.button import Button

class TheApp(App):
    def build(self):
        layout = StackLayout()
        text=open('pyt.txt').readlines()
        print(text[1])
        while(text[i]!='pytanie'):
            odpowiedzi=
        odpowiedzi=['Sortowanie bąbelkowe', 'Sortowanie przez wstawianie', 'Sortowaie przez wybieranie', 'Złożoność O(logn)', 'Złożoność O(n)','Złożoność O(n^2)','Złożoność O(nlogn)']
        layout.add_widget(Label(text='Zaznacz odpowiedzi które dotyczą obrazka. Może być więcej niż jedna prawidłowa odpowiedź.', height=50, size_hint=(1,None)))
        layout.add_widget(Image(source='sort.png', size_hint=(1,None)))
        # Odpowiedzi do zaznaczenia:
        self.tablica = [CheckBox( height=50, size_hint=(0.3, None))]
        j=0
        for i in odpowiedzi:
            self.tablica.append(CheckBox( height=50, size_hint=(0.3, None)))
            layout.add_widget(self.tablica[j])
            layout.add_widget( Label( text=i, height=50, size_hint=(0.7, None) ) )
            j=j+1
        self.ifOk = Button( text="Sprawdź!", size_hint=(.5, .2), on_press=self.check )
        layout.add_widget( self.ifOk )
        return layout

    def check(self,event):
        if(self.tablica[0].active and self.tablica[5].active):
           self.ifOk.text='Świetnie! Przejdź do następnego pytania :)'
        else:
            self.ifOk.text='Niestety to nie jest dobra odpowiedź, spróbuj jeszcze raz'

TheApp().run()