# -*- coding: utf-8 -*-
import sys
import pika  
import time
from threading import Thread
from SOAPpy import SOAPServer
from omniORB import CORBA, PortableServer
import CosNaming, MainServer, MainServer__POA
import server_client_side as client_side  

connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# Cria a fila de mensagens para o usuário 
def create_queue(user_name):
    channel.queue_declare(queue = user_name)

soap_server = SOAPServer(('localhost', 8081))
soap_server.registerFunction(create_queue)

def server_run():
    soap_server.serve_forever()

# Executa o webservice em uma thread, pois o processo é bloqueante
go_server = Thread(target = server_run)
go_server.daemon = True
go_server.start()

class MainServer(MainServer__POA.Server):
    users = [] # [[username, obj], [username, obj], [username, obj]...]
    
    # Informa para o cliente se o username está cadastrado no servidor
    def username_is_registered(self, username):
        if username in [user[0] for user in self.users]:
            return True
        return False

    # Recebe o username do novo usuário 
    def receive_username(self, user_name):     
        print("entrei no receive_username do servidor")
        # Se o username não estiver na lista de usuários
        if user_name not in [user[0] for user in self.users]:
            obj = client_side.bind(user_name)   # conecta o servidor ao novo cliente
            self.users.append([user_name, obj]) # adiciona o username na lista de usuários
            print("{} registrado com sucesso").format(user_name)
        else:
            print("\n ***** Já existe um usuário cadastrado com este nome! *****\n\n")

    def send_status(self, user_name, new_status):
        if user_name != [user[0] for user in self.users]:
            user[1].update_contacts_status(user_name, new_status)

    def send_msg(self, sender, receiver, msg, timestamp):
        print("!!! entrei no send_msg do servidor !!!")
        
        for index, user in enumerate(self.users):
            if receiver == user[0]:
                print(index)
                # Se o destinatário da mensagem estiver online, 
                # envia a mensagem por Corba
                if self.users[index][1].return_status() is True: 
                    print("TA ONLINE")
                    self.users[index][1].receive_msg(sender, receiver, msg, timestamp)
                
                # Se o destinatário da mensagem estiver offline,
                # adiciona a mensagem na sua fila de mensagens
                elif self.users[index][1].return_status() is False:
                    print("TA OFFLINE")
                    channel.basic_publish(exchange = "", 
                                          routing_key = receiver, 
                                          body = timestamp + " " + sender + ": " + msg)

# Initialise the ORB and find the root POA
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")

# Create an instance of Server and an Server object reference
ei = MainServer()
eo = ei._this()

# Obtain a reference to the root naming context
obj = orb.resolve_initial_references("NameService")
rootContext = obj._narrow(CosNaming.NamingContext)

if rootContext is None:
    print("Failed to narrow the root naming context")
    sys.exit(1)

# Bind context to the root context
try:
    name = [CosNaming.NameComponent("mainServer", "context")]
    context = rootContext.bind_new_context(name)
    print("New context bounded: {}".format("mainServer"))

except CosNaming.NamingContext.AlreadyBound, ex:
    obj = rootContext.resolve(name)
    context = obj._narrow(CosNaming.NamingContext)
    
    if context is None:
        print "context exists but is not a NamingContext"
        sys.exit(1)
    
# Bind the object to the context
try:
    name = [CosNaming.NameComponent("Server", "Object")]
    context.bind(name, eo)

except CosNaming.NamingContext.AlreadyBound:
    context.rebind(name, eo)

# Activate the POA
poaManager = poa._get_the_POAManager()
poaManager.activate()

# Block for ever (or until the ORB is shut down)
orb.run()