"""
Provides DBus services for Support and Health monitoring.

:Bus:
    ``session``
:Busname:
    ``{{ cookiecutter.dbus_bus_name }}``
:ObjectPath:
    ``{{ cookiecutter.dbus_support_object_path }}``
:Interface:
    ``{{ cookiecutter.dbus_support_interface }}``
"""

import dbus
import dbus.service
import json

from gwn.helpers.logger import logger

from . import BUSNAME, SUPPORT_OBJECTPATH, SUPPORT_INTERFACE



class SupportService( dbus.service.Object ):

    def __init__( self ):
        bus_name = dbus.service.BusName( BUSNAME, bus = dbus.SessionBus() )
        super().__init__( bus_name = bus_name, object_path = SUPPORT_OBJECTPATH )


    @dbus.service.method( SUPPORT_INTERFACE, out_signature = 's' )
    def GetState( self ):
        """
        Return the current runtime state of the service.

        Returns:
            str: json encoded, free-form-ish dictionary of runtime state information
        """
        return json.dumps( {} )


    @dbus.service.method( SUPPORT_INTERFACE, out_signature = 's' )
    def GetLogLevel( self ):
        """
        Return the current log level.

        Returns:
            str: a logging level, e.g. ``"debug"``, ``"info"``, ``"warning"``, etc.
        """
        return logger.getLevel()


    @dbus.service.method( SUPPORT_INTERFACE, in_signature = 's' )
    def SetLogLevel( self, level ):
        """
        Set the effective log level.

        Args:
            level (str): the desired log level, e.g. ``"debug"``, ``"warning"``

        Raises:
            ValueError: if ``level`` is not a valid log level name

        Notes:

            * This method changes the log level for the duration of this runtime. The log level will
              return to the default if this process is restarted.
        """
        level = str( level )
        if level.lower() in { 'critical', 'error', 'warning', 'info', 'debug', 'notset' }:
            logger.setLevel( level )
        else:
            raise ValueError( 'unknown log level: {!r}'.format( level ) )

