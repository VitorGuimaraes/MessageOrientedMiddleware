# Interface
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

# Layouts
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

# Widgets
from kivy.uix.image import Image 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 

from kivy.uix.screenmanager import ScreenManager, Screen
from contact_box import ContactBox

class Run(Screen):
    def __init__(self, tarefas, **kwargs):
        super(Run, self).__init__(**kwargs)

        self.scroll_view = ScrollView()
        self.scroll_view.orientation = "vertical"

        self.box = BoxLayout()
        self.scroll_view.add_widget(self.box)

        self.box.orientation = "vertical"
        self.box.size_hint_y = None
        self.box.bind(minimum_height = self.box.setter("height")) 

        for tarefa in tarefas:
            # self.box.add_widget(Button(text = tarefa, font_size = 30, size_hint_y = None, height = 200))
            self.box.add_widget(ContactBox(tarefa, size_hint_y = None, width = 402, height = 80))

        self.add_widget(self.scroll_view)

class Test(App):
    def build(self):
        return Run(["A", "B", "C", "D", "E"])

Test().run()