
import dbus.service

from gwn.logger import logger

from . import BUSNAME, OBJECTPATH, INTERFACE
from .foo import foo



class FooService( dbus.service.Object ):

    def __init__( self ):
        bus_name = dbus.service.BusName( BUSNAME, bus = dbus.SessionBus() )
        super().__init__( bus_name = bus_name, object_path = OBJECTPATH )
        logger.info( 'connected to system bus' )


    @dbus.service.method( INTERFACE, out_signature = 'i' )
    def Foo( self ):
        return foo()

