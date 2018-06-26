# -*- coding: utf-8 -*-
import sys
from threading import Thread # Thread usada para iniciar o orb do Corba
import time
from SOAPpy import SOAPProxy
import pika 
from omniORB import CORBA, PortableServer
import CosNaming, MainClient, MainClient__POA
import client_client_side as client_side 
from contact import Contact

# Interface
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config

# Layouts
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView

# Widgets
from kivy.uix.image import Image 
from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.uix.textinput import TextInput 
from contact_box import ContactBox

# Configuração da tela
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '715')

# Colocar depois de todas as configurações e imports, senão afeta a aplicação
from kivy.core.window import Window 
Window.clearcolor = (1, 1, 1, 1)

soap_server = SOAPProxy("http://localhost:8081/")

# Registra o usuário no nameserver com seu username
my_username = ""
new_contact_added = ""
contacts = []

# Retorna o objeto do servidor para invocar seus métodos
server_obj = client_side.bind()

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

class MasterClient(MainClient__POA.Client):
    
    # Tela de registro
    class Register(FloatLayout):
        def __init__(self, **kwargs):
            super(MasterClient.Register, self).__init__(**kwargs)

            # Background image
            self.background = Image()
            self.background.source = ("interface/Register/register.png")

            # Next button
            self.next_button = Button()
            self.next_button.size = (25, 25)
            self.next_button.pos = (360, 645)
            self.next_button.background_color = (1.0, 1.0, 1.0, 0.01) 
            self.next_button.on_press = self.dismiss_Register

            # TextInput field
            self.username = TextInput()
            self.username.size = (240, 29)
            self.username.pos = (113, 545) 
            self.username.font_name = "interface/Montserrat-Medium.ttf"
            self.username.font_size = 14
            self.username.cursor_color = [0.31, 0.49, 0.63, 1.0]
            self.username.background_color = (1.0, 1.0, 1.0, 0)

            self.background.add_widget(self.next_button)
            self.background.add_widget(self.username)
            self.add_widget(self.background)

        def dismiss_Register(self):
            global my_username
            my_username = str(self.username.text)
            self.clear_widgets()
            # Para a GUI para que a execução de conexão possa continuar
            App.get_running_app().stop() 

    class Home(Screen):
        def __init__(self, ms, **kwargs):
            super(MasterClient.Home, self).__init__(**kwargs)

            self.ms = ms
            
            # Float Layout Top Bar
            self.float_layout = FloatLayout()
            self.float_layout.size_hint = (None, None)
            # self.float_layout.pos_hint = (None, None) # Não pode definir no FloatLayout
            self.float_layout.size = (402, 85)
            self.float_layout.y = 630
            
            # Top Bar image
            self.top_bar = Image()
            self.float_layout.add_widget(self.top_bar)
            self.top_bar.source = ("interface/Home/top_bar1.png")
            self.top_bar.y = 630

            # AddContact button
            self.add_contact_btn = Button()
            self.float_layout.add_widget(self.add_contact_btn)
            self.add_contact_btn.size_hint = (None, None)
            self.add_contact_btn.size = (40, 40)
            self.add_contact_btn.pos = (345, 643)
            self.add_contact_btn.background_color = (1.0, 1.0, 1.0, 0) 
            self.add_contact_btn.on_press = self.press_add_contact_button
            
            # Switch status button
            self.switch_status = Button()
            self.float_layout.add_widget(self.switch_status)
            self.switch_status.size_hint = (None, None)
            self.switch_status.size = (43, 24)
            self.switch_status.pos = (20, 651)
            self.switch_status.background_color = (1.0, 1.0, 1.0, 0)
            self.switch_status.on_press = self.press_switch_status

            # Switch status image
            self.switch_img = Image()
            self.add_widget(self.float_layout)
            self.switch_status.add_widget(self.switch_img)
            self.switch_img.source = ("interface/Home/switch_on.png")
            self.switch_img.size = (43, 24)
            self.switch_img.pos = (20, 651)

            # Scroll View
            self.scroll_view = ScrollView() 
            self.add_widget(self.scroll_view)
            self.scroll_view.size_hint = (None, None)
            self.scroll_view.size = (402, 630) 
            self.scroll_view.y = self.scroll_view.parent.x
            self.scroll_view.orientation = "vertical"
            self.scroll_view.background_color = (255, 0, 0, 1)
            
            # Box View chats
            self.box = BoxLayout() 
            self.scroll_view.add_widget(self.box)
            self.box.id = "box"
            self.box.orientation = "vertical"
            self.box.size_hint_y = None
            self.box.bind(minimum_height = self.box.setter("height")) 
            self.box.y = self.box.parent.y

            print(len(contacts))
            for contact in contacts: 
                print("entrei aqui no coisa do bicho do negoço")
                print(contact)
                ###
                # Box button
                box_button = Button()
                self.box.add_widget(box_button)

                box_button.size_hint = (None, None)
                box_button.width = 402
                box_button.height = 80
                #box_button.background_color = (255, 255, 255, 1)

                # Contact photo image
                contact_photo = Image()
                box_button.add_widget(contact_photo)
                contact_photo.source = ("interface/Home/contact.png")
                contact_photo.size_hint = (None, None)
                contact_photo.pos_hint = (None, None)
                contact_photo.size = (80, 80)
                contact_photo.pos = (0, 0)
                
                # Contact status img
                contact_img_status = Image()
                box_button.add_widget(contact_img_status)
                contact_img_status.source = ("interface/online.png")
                contact_img_status.size_hint = (None, None)
                contact_img_status.pos_hint = (None, None)
                contact_img_status.size = (80, 80)
                contact_img_status.pos = (330, contact_img_status.parent.y)
                
                # Contact name label
                lbl_name = Label()
                box_button.add_widget(lbl_name)
                lbl_name.text = contact_name
                lbl_name.size = (15, 120)
                lbl_name.pos = (90, contact_img_status.parent.y)
                ###

        def press_switch_status(self):
            if self.switch_img.source == ("interface/Home/switch_on.png"):
                self.switch_img.source = ("interface/Home/switch_off.png")
            else:
                self.switch_img.source = ("interface/Home/switch_on.png")
            self.ms.set_my_status()

        def press_add_contact_button(self): 
            App.get_running_app().sm.current = "addcontact"

        # def add_contact_box(self, new_contact_added):
        #     self.box.add_widget(ContactBox(new_contact_added))

    class AddContact(Screen):
        def __init__(self, ms, home_screen, **kwargs):
            super(MasterClient.AddContact, self).__init__(**kwargs)

            self.ms = ms
            self.home_screen = home_screen

            self.layout = FloatLayout()
            # Background image
            self.background = Image()
            self.background.source = ("interface/AddContact/add_contact.png")

            # Next button
            self.next_button = Button()
            self.next_button.size = (25, 25)
            self.next_button.pos = (360, 645)
            self.next_button.background_color = (1.0, 1.0, 1.0, 0.5) 
            self.next_button.on_press = self.add_contact

            # TextInput field
            self.contact_username = TextInput()
            self.contact_username.size = (240, 28)
            self.contact_username.pos = (113, 545) 
            self.contact_username.font_name = "interface/Montserrat-Medium.ttf"
            self.contact_username.font_size = 14
            self.contact_username.cursor_color = [0.31, 0.49, 0.63, 1.0]
            self.contact_username.background_color = (1.0, 1.0, 1.0, 0)

            self.background.add_widget(self.next_button)
            self.background.add_widget(self.contact_username)
            self.layout.add_widget(self.background)

            self.add_widget(self.layout)
            
        def add_contact(self):
            new_contact_added = str(self.contact_username.text)
            self.ms.add_contact(new_contact_added)
            
            App.get_running_app().sm.current = "home"

    class Chat(Screen):
        def __init__(self, ms, **kwargs):
            super(MasterClient.Chat, self).__init__(**kwargs)
            
            self.ms = ms
            
            self.layout = FloatLayout()

            # Background image
            self.background = Image()
            self.background.source = ("interface/Chat/chat_bars.png")

            # Back button
            self.back_button = Button()
            self.back_button.size = (25, 25)
            self.back_button.pos = (20, 645)
            self.back_button.background_color = (1.0, 1.0, 1.0, 0.5) 
            self.back_button.on_press = self.back_home

            # Contact status
            self.contact_status = Image()
            self.contact_status.source = ("interface/online.png")
            self.contact_status.size = (18, 18)
            self.contact_status.pos = (360, 652)

            self.background.add_widget(self.back_button)
            self.background.add_widget(self.contact_status)
            self.layout.add_widget(self.background)

            self.add_widget(self.layout)

        def back_home(self):
            App.get_running_app().sm.current = "home" 

    ############ Master Client ############

    status = True

    def kill_consumer():
        channel.stop_consuming()

    connection.add_timeout(0, kill_consumer)

    def return_status(self):
        return self.status

    def set_my_status(self):
        if self.status is True:
            self.status = False
        
        elif self.status is False:   
            self.status = True

            channel.start_consuming() 
            for methods, properties, body in channel.consume(my_username):
                print(body)
            channel.stop_consuming()
            print("Consumação finalizada")

        server_obj.send_status(my_username, self.status)

    # Acho que ta errado. Vai ficar parecido com o metodo send_msg do servidor
    def update_contacts_status(self, user_name, new_status):
        if user_name in [contact.name for contact in contacts]:
            contact.status = new_status
        
    # Adiciona um contato se o username existir na lista de usuários cadastrados
    def add_contact(self, contact_name):
        print("entrei no add_contact do cliente")
        server_username = server_obj.username_is_registered(contact_name)
        print(server_username)
        if server_username is True:
            print("O contato existe no servidor e foi adicionado")
            new_contact = Contact(contact_name)
            contacts.append(new_contact)

            # for contact in contacts:
            #     print contact

    # Envia mensagem para um contato
    def send_msg(self, sender, receiver, msg, timestamp):
        print("entrei no send_msg do cliente e os dados são: ")
        print(sender, receiver, msg, timestamp)

        server_obj.send_msg(my_username, receiver, msg, timestamp)

    # Recebe mensagem enviada pelo servidor
    def receive_msg(self, sender, receiver, msg, timestamp):
        print("{} {}: {}").format(timestamp, sender, msg)

class runRegister(App):
    def build(self):
        return MasterClient().Register() 

runRegister().run()

##################### Corba Configuration #####################

# Initialise the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of Client and an Client object reference
ei = MasterClient()
eo = ei._this()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Failed to narrow the root naming context")
    sys.exit(1)

# Bind context to the root context
try:
    name = [CosNaming.NameComponent(my_username, "context")]
    context = rootContext.bind_new_context(name)
    print("New context bounded: {}".format(my_username))

except CosNaming.NamingContext.AlreadyBound, ex:
    obj = rootContext.resolve(name)
    context = obj._narrow(CosNaming.NamingContext)
    
    if context is None:
        print "context exists but is not a NamingContext"
        sys.exit(1)
   
# Bind the object to the context
try:
    name = [CosNaming.NameComponent("Client", "Object")]
    context.bind(name, eo)

except CosNaming.NamingContext.AlreadyBound:
    context.rebind(name, eo)

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Solicita que o servidor crie uma fila de mensagens
soap_server.create_queue(my_username)

# Registra o username no servidor
server_obj.receive_username(my_username)

# Block for ever (or until the ORB is shut down)
def run_orb():
    orb.run()
    
go_orb = Thread(target = run_orb)	   
go_orb.daemon = True
go_orb.start() 

class RunHome(App):
    sm = ScreenManager()
    
    def build(self):    
        home_screen = MasterClient.Home(ei, name = "home")
        # RunHome.sm.add_widget(MasterClient.Home(ei, name = "home"))
        RunHome.sm.add_widget(home_screen)
        RunHome.sm.add_widget(MasterClient.AddContact(ei, home_screen, name = "addcontact"))
        RunHome.sm.add_widget(MasterClient.Chat(ei, name = "chat"))
        
        return RunHome.sm

def interface_run():
    RunHome().run()

go_thread = Thread(target = interface_run)
go_thread.daemon = True
go_thread.start()

while True:
    print("1 - Adicionar Contato")
    print("2 - Enviar mensagem para Contato")
    print("3 - Alterar Status")
    print("4 - Listar Contatos")
    print("5 - Limpar tela")

    if ei.status is True:
        print("\nVocê está online")    

    elif ei.status is False:
        print("\nVocê está offline")    

    option = int(raw_input("\nOpção: ")) 

    if option is 1:
        contact_name = raw_input("\nNome do contato: ")
        ei.add_contact(contact_name)
    
    elif option is 2:
        contact_name = raw_input("\nNome do contato: ")
        message = raw_input("\nMensagem: ")
        timestamp = time.strftime("%H:%M:%S")
        ei.send_msg(my_username, contact_name, message, timestamp)

    elif option is 3:
        ei.set_my_status()
    
    elif option is 4:
        for contact in ei.contacts:
            print(contact)