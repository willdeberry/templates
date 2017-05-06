
import dbus
import pytest



@pytest.fixture( scope = 'session' )
def support_service():
    obj = dbus.SystemBus().get_object( '{{ cookiecutter.dbus_bus_name }}', '{{ cookiecutter.dbus_support_object_path }}' )
    iface = dbus.Interface( obj, dbus_interface = '{{ cookiecutter.dbus_support_interface }}' )
    return iface



def test_log_level( support_service ):
    support_service.SetLogLevel( 'debug' )

    support_service.SetLogLevel( 'info' )
    assert 'info' == support_service.GetLogLevel()

    support_service.SetLogLevel( 'debug' )
    assert 'debug' == support_service.GetLogLevel()

    support_service.SetLogLevel( 'warning' )
    assert 'warning' == support_service.GetLogLevel()

