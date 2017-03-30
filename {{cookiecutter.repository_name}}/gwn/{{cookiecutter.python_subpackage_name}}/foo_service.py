"""
Provides DBus services for the ultimate question of life, the universe, and everything.

:Bus:
    ``session``
:Busname:
    ``{{ cookiecutter.dbus_bus_name }}``
:ObjectPath:
    ``{{ cookiecutter.dbus_object_path }}``
:Interface:
    ``{{ cookiecutter.dbus_interface }}``

Examples:

    ::

        from gwn.helpers.dbus import find_gwn_service

        {{ cookiecutter.dbus_bus_name[23:-1] }}_service = find_gwn_service(
            bus = 'session',
            bus_name = '{{ cookiecutter.dbus_bus_name[23:] }}',
            object_path = '{{ cookiecutter.dbus_object_path[24:] }}',
            interface = '{{ cookiecutter.dbus_interface[23:] }}'
        )
"""

import dbus.service

from gwn.helpers.logger import logger

from . import BUSNAME, OBJECTPATH, INTERFACE
from .foo import foo



class FooService( dbus.service.Object ):

    def __init__( self ):
        bus_name = dbus.service.BusName( BUSNAME, bus = dbus.SessionBus() )
        super().__init__( bus_name = bus_name, object_path = OBJECTPATH )
        logger.info( 'connected to session bus' )


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

