
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository.GObject import MainLoop

from gwn.logger import logger

from .foo_service import FooService



def main():
    DBusGMainLoop( set_as_default = True )

    service = FooService()

    try:
        logger.debug( 'entering main loop' )
        MainLoop().run()
    except KeyboardInterrupt:
        pass

