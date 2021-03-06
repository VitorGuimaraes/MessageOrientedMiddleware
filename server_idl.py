# Python stubs generated by omniidl from server.idl
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
# Start of module "MainServer"
#
__name__ = "MainServer"
_0_MainServer = omniORB.openModule("MainServer", r"server.idl")
_0_MainServer__POA = omniORB.openModule("MainServer__POA", r"server.idl")


# interface Server
_0_MainServer._d_Server = (omniORB.tcInternal.tv_objref, "IDL:MainServer/Server:1.0", "Server")
omniORB.typeMapping["IDL:MainServer/Server:1.0"] = _0_MainServer._d_Server
_0_MainServer.Server = omniORB.newEmptyClass()
class Server :
    _NP_RepositoryId = _0_MainServer._d_Server[1]

    def __init__(self, *args, **kw):
        raise RuntimeError("Cannot construct objects of this type.")

    _nil = CORBA.Object._nil


_0_MainServer.Server = Server
_0_MainServer._tc_Server = omniORB.tcInternal.createTypeCode(_0_MainServer._d_Server)
omniORB.registerType(Server._NP_RepositoryId, _0_MainServer._d_Server, _0_MainServer._tc_Server)

# Server operations and attributes
Server._d_receive_username = (((omniORB.tcInternal.tv_string,0), ), (), None)
Server._d_send_msg = (((omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0), (omniORB.tcInternal.tv_string,0)), (), None)
Server._d_send_status = (((omniORB.tcInternal.tv_string,0), omniORB.tcInternal.tv_boolean), (), None)
Server._d_username_is_registered = (((omniORB.tcInternal.tv_string,0), ), (omniORB.tcInternal.tv_boolean, ), None)

# Server object reference
class _objref_Server (CORBA.Object):
    _NP_RepositoryId = Server._NP_RepositoryId

    def __init__(self, obj):
        CORBA.Object.__init__(self, obj)

    def receive_username(self, *args):
        return self._obj.invoke("receive_username", _0_MainServer.Server._d_receive_username, args)

    def send_msg(self, *args):
        return self._obj.invoke("send_msg", _0_MainServer.Server._d_send_msg, args)

    def send_status(self, *args):
        return self._obj.invoke("send_status", _0_MainServer.Server._d_send_status, args)

    def username_is_registered(self, *args):
        return self._obj.invoke("username_is_registered", _0_MainServer.Server._d_username_is_registered, args)

omniORB.registerObjref(Server._NP_RepositoryId, _objref_Server)
_0_MainServer._objref_Server = _objref_Server
del Server, _objref_Server

# Server skeleton
__name__ = "MainServer__POA"
class Server (PortableServer.Servant):
    _NP_RepositoryId = _0_MainServer.Server._NP_RepositoryId


    _omni_op_d = {"receive_username": _0_MainServer.Server._d_receive_username, "send_msg": _0_MainServer.Server._d_send_msg, "send_status": _0_MainServer.Server._d_send_status, "username_is_registered": _0_MainServer.Server._d_username_is_registered}

Server._omni_skeleton = Server
_0_MainServer__POA.Server = Server
omniORB.registerSkeleton(Server._NP_RepositoryId, Server)
del Server
__name__ = "MainServer"

#
# End of module "MainServer"
#
__name__ = "server_idl"

_exported_modules = ( "MainServer", )

# The end.
