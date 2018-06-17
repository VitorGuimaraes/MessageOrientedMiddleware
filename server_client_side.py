# -*- coding: utf-8 -*-
import sys
import os
import time
from omniORB import CORBA, PortableServer
import CosNaming, MainClient, MainClient__POA

# Define funções para que o servidor possa invocar
# os métodos remotos dos outros clientes

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Conecta o servidor ao cliente passado por parâmetro
def bind(user_name):
    try:
        obj = orb.resolve_initial_references("NameService")
        rootContext = obj._narrow(CosNaming.NamingContext)
        
        name = [CosNaming.NameComponent(user_name, "context"),
        CosNaming.NameComponent("Client", "Object")]
        
        obj = rootContext.resolve(name)
        obj = obj._narrow(MainClient.Client)
        
        print("Server connected to {} ".format(user_name))
            
    except:
        print("Trying to connect to user {}...".format(user_name))
        time.sleep(1)
        bind(user_name)

    return obj