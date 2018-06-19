# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button 

class Master():
    class Menu(Screen):
        def __init__(self, **kwargs):
            super(Master.Menu, self).__init__(**kwargs)

            self.add_contact_btn = Button()
            self.add_contact_btn.size_hint = (None, None)
            self.add_contact_btn.size = (40, 40)
            self.add_contact_btn.pos = (0, 45)
            self.add_contact_btn.background_color = (1.0, 0.5, 1.0, 1) 

            self.add_contact_btn.on_press = self.pressed

            self.add_widget(self.add_contact_btn)

        def pressed(self):
            App.get_running_app().sm.current = "game"

    class Game(Screen):
        def __init__(self, **kwargs):
            super(Master.Game, self).__init__(**kwargs)

            self.add_contact_btn = Button()
            self.add_contact_btn.size_hint = (None, None)
            self.add_contact_btn.size = (70, 70)
            self.add_contact_btn.pos = (0, 45)
            self.add_contact_btn.background_color = (1.0, 0.5, 1.0, 1) 
            
            self.add_contact_btn.on_press = self.pressed

            self.add_widget(self.add_contact_btn)

        def pressed(self):
            App.get_running_app().sm.current = "menu"
    
    class Test(FloatLayout):
        def __init__(self, **kwargs):
            super(Master.Test, self).__init__(**kwargs)

            self.add_contact_btn = Button()
            self.add_contact_btn.size_hint = (None, None)
            self.add_contact_btn.size = (120, 120)
            self.add_contact_btn.pos = (0, 60)
            self.add_contact_btn.background_color = (1.0, 0.5, 1.0, 1) 

            self.add_contact_btn.on_press = self.pressed

            self.add_widget(self.add_contact_btn)

        def pressed(self):
            App.get_running_app().stop()

class Runner1(App):
    def build(self):       
        return Master().Test()

Runner1().run()

class Runner(App):
    sm = ScreenManager()

    def build(self):
        Runner.sm.add_widget(Master.Menu(name = "menu"))
        Runner.sm.add_widget(Master.Game(name = "game"))
        
        return Runner.sm
Runner().run()