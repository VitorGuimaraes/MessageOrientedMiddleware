# -*- coding: utf-8 -*-
import sys
import os
from omniORB import CORBA, PortableServer
import CosNaming, Agenda, Agenda__POA

# Define o comportamento cliente que o servidor assume para poder invocar
# os métodos remotos dos outros servidores agendas

names = ["agenda1", "agenda2", "agenda3"]
orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)

# Remove da lista o nome da agenda que está chamando os métodos remotos
# das demais agendas. Assim chamará os métodos apenas das outras agendas, 
# e não de si mesma
def check():
    choose = False
    while not choose:
        print("*** Escolha o servidor ***")
        print("1 - agenda1")
        print("2 - agenda2")
        print("3 - agenda3")
        try: 
            name_server = int(raw_input("Servidor Selecionado: "))
            if name_server in range(1, 4):
                server = names[name_server-1]
                del(names[name_server-1])
                choose = True
                return server
        except:
            print("\n***** Opção inválida! Tente novamente! ***** \n\n")

# Verifica quais agendas estão online e insere um obj._narrow para cada uma
# em uma lista
def bind():
    remote_obj = []
    for server_name in names:
        try:
            obj = orb.resolve_initial_references("NameService")
            rootContext = obj._narrow(CosNaming.NamingContext)
            name = [CosNaming.NameComponent(server_name, "context"),
            CosNaming.NameComponent("Schedule", "Object")]
            
            obj = rootContext.resolve(name)
            obj = obj._narrow(Agenda.Schedule)
            obj.isOnline()
            
            print("{} is ONLINE  :D".format(server_name))
            remote_obj.append(obj)
            
        except:
            print("{} is offline :(".format(server_name))
    return remote_obj

def add(name, phone):
    remote_obj = bind()
    if len(remote_obj) > 0:
        for obj in remote_obj:
            obj.add(name, phone)

def remove(index_name):
    remote_obj = bind()
    if len(remote_obj) > 0:
        for obj in remote_obj:
            obj.remove(index_name) 

def edit(index_name, new_name, new_phone):
    remote_obj = bind()
    if len(remote_obj) > 0:
        for obj in remote_obj:
            # Chama a função edit das outras agendas
            obj.edit(index_name, new_name, new_phone)
            obj.search()

def backup():
    remote_obj = bind()
    
    if len(remote_obj) > 0:
        names = []
        phones = []
        contacts_size = remote_obj[0].get_contacts_size()
        for i in range(contacts_size):
            names.append(remote_obj[0].get_names(i))
            phones.append(remote_obj[0].get_phones(i))
        return names, phones
    return None, None