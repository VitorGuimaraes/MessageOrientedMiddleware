import kivy

from kivy.app import App
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.widget import Widget

class CustTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustTextInput, self).__init__(**kwargs) 
        self.widget = TextInput()
        self.widget.size = 300, 50
        self.widget.color = (.10, .9, 1, 2)

class CustButton(Button):
    def __init__(self, **kwargs):
        super(CustButton, self).__init__(**kwargs) 
        self.font_size = 16
        self.size = (100, 50)

class TheWidget(Widget):
    def __init__(self, **kwargs):
        super(TheWidget, self).__init__(**kwargs) 
            
        self.name_input = CustTextInput()
        self.name_input.hint_text = "First Name"
        # self.name_input.pos = self.name_input.parent.x, (self.name_input.parent.height / 2) + 250

        self.surname_input = CustTextInput()
        self.surname_input.hint_text = "Last Name"
        # self.surname_input.pos = self.surname_input.parent.x, (self.surname_input.parent.height / 2) + 180

        self.lbl = Label()
        self.lbl.text = ""
        # self.lbl.pos = self.lbl.parent.x + 400, (self.lbl.parent.height / 2) + 190
        self.lbl.color = 244, 65, 223, 1

        self.submit = CustButton()
        # self.submit.pos = self.submit.parent.x + 310, (self.submit.parent.height / 2) + 210
        # self.submit.on_press = inp.text = ""
            # on_press: inp2.text = ""
            # on_press: label.text = "Submitted"
            # on_press: self.disabled = True

        self.add_widget(self.name_input)
        self.add_widget(self.surname_input)
        self.add_widget(self.lbl)
        self.add_widget(self.submit)

# class TheWidget(Widget):
    # pass

class WidgetsApp(App):
    # This returns the content we want in the window
    def build(self):
        # Return a the TheWidget Class
        return TheWidget()

if __name__ == "__main__":
    widgetsapp = WidgetsApp()
    widgetsapp.run()