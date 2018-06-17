# Python stubs generated by omniidl from client.idl
# DO NOT EDIT THIS FILE!

import omniORB, _omnipy
from omniORB import CORBA, PortableServer
_0_CORBA = CORBA


_omnipy.checkVersion(4,2, __file__, 1)

try:
    property
except NameError:
    def property(*args):
        return None


#
# Start of module "MainClient"
#
__name__ = "MainClient"
_0_MainClient = omniORB.openModule("MainClient", r"client.idl")
_0_MainClient__POA = omniORB.openModule("MainClient__POA", r"client.idl")


# interface Client
_0_MainClient._d_Client = (omniORB.tcInternal.tv_objref, "IDL:MainClient/Client:1.0", "Client")
omniORB.typeMapping["IDL:MainClient/Client:1.0"] = _0_MainClient._d_Client
_0_MainClient.Client = omniORB.newEmptyClass()
class Client :
    _NP_RepositoryId = _0_MainClient._d_Client[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_MainClient.Client = Client
_0_MainClient._tc_Client = omniORB.tcInternal.createTypeCode(_0_MainClient._d_Client)
omniORB.registerType(Client._NP_RepositoryId, _0_MainClient._d_Client, _0_MainClient._tc_Client)

# Client operations and attributes
Client._d_receive_msg = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)
Client._d_update_contacts_status = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)

# Client object reference
class _objref_Client (CORBA.Object):
    _NP_RepositoryId = Client._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def receive_msg(self, *args):
        return self._obj.invoke("receive_msg", _0_MainClient.Client._d_receive_msg, args)

    def update_contacts_status(self, *args):
        return self._obj.invoke("update_contacts_status", _0_MainClient.Client._d_update_contacts_status, args)

omniORB.registerObjref(Client._NP_RepositoryId, _objref_Client)
_0_MainClient._objref_Client = _objref_Client
del Client, _objref_Client

# Client skeleton
__name__ = "MainClient__POA"
class Client (PortableServer.Servant):
    _NP_RepositoryId = _0_MainClient.Client._NP_RepositoryId


    _omni_op_d = {"receive_msg": _0_MainClient.Client._d_receive_msg, "update_contacts_status": _0_MainClient.Client._d_update_contacts_status}

Client._omni_skeleton = Client
_0_MainClient__POA.Client = Client
omniORB.registerSkeleton(Client._NP_RepositoryId, Client)
del Client
__name__ = "MainClient"

#
# End of module "MainClient"
#
__name__ = "client_idl"

_exported_modules = ( "MainClient", )

# The end.
