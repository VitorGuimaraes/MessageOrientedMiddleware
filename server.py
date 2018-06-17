# -*- coding: utf-8 -*-
import sys
import pika  
import time
from omniORB import CORBA, PortableServer
import CosNaming, MainServer, MainServer__POA
import server_client_side as client_side  
 
class MainServer(MainServer__POA.Server):
    users = [] # [[username, obj], [username, obj], [username, obj]...]
    
    def server_users_list(self):
        return [user[0] for user in self.users]

    # Recebe o username do novo usuário 
    def receive_username(self, user_name):     
        # Se o username não estiver na lista de usuários
        time.sleep(2)
        if user_name not in [user[0] for user in self.users]:
            obj = client_side.bind(user_name)   # conecta o servidor ao novo cliente
            self.users.append([user_name, obj]) # adiciona o username na lista de usuários
        else:
            print("\n ***** Já existe um usuário cadastrado com este nome! *****\n\n")

    def send_status(self, user_name, new_status):
        if user_name != [user[0] for user in self.users]:
            user[1].update_contacts_status(user_name, new_status)

    def send_msg(self, sender, receiver, msg, timestamp):
        if receiver == [user[0] for user in users]:
            user[1].receive_msg(sender, receiver, msg, timestamp)
    
    # Métodos que manipulam os métodos dos clientes 
    # (o servidor é cliente dos outros clientes)

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