# -*- coding: utf-8 -*-
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '715')

# Colocar depois de todas as configuraçõese imports, senão afeta a aplicação
from kivy.core.window import Window 
Window.clearcolor = (1, 1, 1, 1)

class BuildRegister(FloatLayout):
    def on_click(self):
        print(self.ids.username.text)
        self.clear_widgets()
        main.root_window.remove_widget(main.root)
        main.root_window.add_widget(BuildHome())

class BuildHome(FloatLayout):
    def add_contact(self):
        self.clear_widgets()
        main.root_window.remove_widget(main.root)
        main.root_window.add_widget(AddContact())

    def open_message(self):
        self.clear_widgets()
        main.root_window.remove_widget(main.root)
        main.root_window.add_widget(Chat())
    
class AddContact(FloatLayout):
    def confirm(self):
        self.clear_widgets()
        main.root_window.remove_widget(main.root)
        main.root_window.add_widget(BuildHome())

class Chat(FloatLayout):
    def back_home(self):
        self.clear_widgets()
        main.root_window.remove_widget(main.root)
        main.root_window.add_widget(BuildHome())

class Interface(App):
    def build(self):
        return BuildRegister()

main = Interface()
main.run()