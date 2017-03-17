
import dbus.service

from gwn.helpers.logger import logger

from . import BUSNAME, OBJECTPATH, INTERFACE
from .foo import foo



class FooService( dbus.service.Object ):
    """
    Provides DBus services for the ultimate question of life, the universe, and everything.

    :Bus:
        ``system``
    :Busname:
        ``{{ cookiecutter.dbus_bus_name }}``
    :ObjectPath:
        ``{{ cookiecutter.dbus_object_path }}``
    :Interface:
        ``{{ cookiecutter.dbus_interface }}``
    """

    def __init__( self ):
        bus_name = dbus.service.BusName( BUSNAME, bus = dbus.SystemBus() )
        super().__init__( bus_name = bus_name, object_path = OBJECTPATH )
        logger.info( 'connected to system bus' )


    @dbus.service.method( INTERFACE, out_signature = 'i' )
    def Foo( self ):
        """
        Returns the answer to the ultimate question of life, the universe, and everything.

        :DBus Signature:
            ``i: outbound``

        Returns:
            int
        """
        return foo()

