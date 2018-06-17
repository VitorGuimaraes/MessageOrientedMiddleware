# -*- coding: utf-8 -*-
import sys
import os
from omniORB import CORBA, PortableServer
import CosNaming, MainServer, MainServer__POA

# Define funções para que o servidor possa invocar
# os métodos remotos dos outros clientes

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Conecta o servidor ao cliente
def bind():
    try:
        obj = orb.resolve_initial_references("NameService")
        rootContext = obj._narrow(CosNaming.NamingContext)
        
        name = [CosNaming.NameComponent("mainServer", "context"),
        CosNaming.NameComponent("Server", "Object")]
        
        obj = rootContext.resolve(name)
        obj = obj._narrow(MainServer.Server)
        
        print("Connected to mainServer")
            
    except:
            print("mainServer is offline")
    return obj