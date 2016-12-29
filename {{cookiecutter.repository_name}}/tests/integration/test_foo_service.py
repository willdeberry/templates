
import dbus
import pytest
import time



@pytest.fixture( scope = 'session' )
def foo_service():
    obj = dbus.SystemBus().get_object( '{{ cookiecutter.dbus_bus_name }}', '{{ cookiecutter.dbus_object_path }}' )
    iface = dbus.Interface( obj, dbus_interface = '{{ cookiecutter.dbus_interface }}' )
    return iface



def test_foo( foo_service ):
    assert foo_service.Foo() == 42

