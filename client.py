# -*- coding: utf-8 -*-
import sys
import time
import pika 
from omniORB import CORBA, PortableServer
import CosNaming, MainClient, MainClient__POA
import client_client_side as client_side 
from contact import Contact

# Interface
import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.config import Config

# Configuração da janela
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '402')
Config.set('graphics', 'height', '715')

# Registra o usuário no nameserver com seu username
my_username = raw_input("Insira seu nome de usuário: ")

# Retorna o objeto do servidor para invocar seus métodos
server_obj = client_side.bind()

class MainClient(MainClient__POA.Client, BoxLayout):
       
    status = 1
    contacts = [] 

    def set_my_status(self):
        if self.status == 1:
            self.set_status = 0
        elif self.status == 0:   
            self.status = 1
        server_obj.send_status(my_username, self.status)

    def update_contacts_status(self, user_name, new_status):
        if user_name in [contact.name for contact in self.contacts]:
            contact.status = new_status

    # Recebe a lista de usuários cadastrados enviada pelo servidor
    def get_server_users_list(self):
        return server_obj.server_users_list()
        
    # Adiciona um contato se o username existir na lista de usuários cadastrados
    def add_contact(self, contact_name):
        server_users = self.get_server_users_list()
        if contact_name in server_users:
            new_contact = Contact(contact_name)
            self.contacts.append(new_contact)

    # Envia mensagem para um contato
    def send_msg(self, sender, receiver, msg, timestamp):
        time = time.strftime("%H:%M:%S")
        if receiver == [contact.name for contact in self.contacts]:
            contact.add_msg(sender, msg, time)
        # server_obj.send_msg(my_username, "amigo_tal", "ola", time)

    # Recebe mensagem enviada pelo servidor
    def receive_msg(self, sender, receiver, msg, timestamp):
        print(sender, receiver)
        print(msg)
        print(timestamp)

# Initialise the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of Client and an Client object reference
ei = MainClient()
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

server_obj.receive_username(my_username)

class Interface(App):
    def build(self):
        return MainClient()

janela = Interface()
janela.run()

# Block for ever (or until the ORB is shut down)
orb.run()