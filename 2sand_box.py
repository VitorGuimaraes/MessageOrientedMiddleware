# Interface
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

# Layouts
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView

# Widgets
from kivy.uix.image import Image 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 

class Tarefas(ScrollView):
    def __init__(self, tarefas, **kwargs):
        super(Tarefas, self).__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Button(text = tarefa, font_size = 30, size_hint_y = None, height = 200))

class Test(App):
    def build(self):
        return Tarefas(["A", "B", "C", "D", "E"])

Test().run()