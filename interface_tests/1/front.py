# -*- coding: utf-8 -*-
import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.config import Config

import CosNaming, MainClient, MainClient__POA

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '715')

class Tela1(MainClient__POA.Client, GridLayout):
    
    def on_press_bt(self):
        # Remove a tela1 do top da hierarquia
        janela.root_window.remove_widget(janela.root)

        # Adiciona uma instância de Tela2 ao topo da hierarquia
        janela.root_window.add_widget(Tela2())

    def add_button(self):
        self.add_widget(Button(text = "new button"))

    # def __init__(self, **kwargs):
    #     super(Tela1, self).__init__(**kwargs)
    #     self.orientation = "vertical"
        
    #     # Criando botão e adicionando ao layout
    #     bt1 = Button(text = "Clique")
    #     # Associa a função on_press_button para ser a função de pressionamento do botão
    #     bt1.on_press = self.on_press_bt
    #     self.add_widget(bt1)

    #     # Criando e adicionando diretamente
    #     self.add_widget(Button(text = "bt2"))
    #     self.add_widget(Button(text = "bt3"))

class Tela2(BoxLayout):

    def on_press_bt(self):
        # Remove a tela2 do top da hierarquia
        janela.root_window.remove_widget(janela.root)

        # Adiciona uma instância de Tela1 ao topo da hierarquia
        janela.root_window.add_widget(Tela1())

    # def __init__(self, **kwargs):
    #     super(Tela2, self).__init__(**kwargs)
    #     self.orientation = "vertical"
    #     bt = Button(text = "Clique")
    #     bt.on_press = self.on_press_bt
    #     self.add_widget(bt)

class KVvsPY(App):
    pass
    # def build(self):
        # return Tela1()

janela = KVvsPY()
janela.run()