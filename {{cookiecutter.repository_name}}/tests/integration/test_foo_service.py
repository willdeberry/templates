
import dbus
import os
import pwd
import pytest
import time



@pytest.yield_fixture( scope = 'session' )
def start_unit():
    bus = dbus.SessionBus()
    manager = bus.get_object( 'org.freedesktop.systemd1', '/org/freedesktop/systemd1' )
    manager = dbus.Interface( manager, 'org.freedesktop.systemd1.Manager' )

    unit = manager.LoadUnit( '{{ cookiecutter.systemd_service_name }}.service' )
    unit = bus.get_object( 'org.freedesktop.systemd1', unit )
    unit_properties = dbus.Interface( unit, 'org.freedesktop.DBus.Properties' )
    unit = dbus.Interface( unit, 'org.freedesktop.systemd1.Unit' )
    get_state = lambda: unit_properties.Get( 'org.freedesktop.systemd1.Unit', 'ActiveState' )

    if get_state() != 'active':
        unit.Start( 'replace' )
        deadline = time.time() + 5

        while get_state() != 'active' and time.time() < deadline:
            time.sleep( 0.05 )
        assert get_state() == 'active'

        yield unit

        unit.Stop( 'replace' )
    else:
        yield unit



@pytest.fixture( scope = 'session' )
def foo_service( start_unit ):
    obj = dbus.SessionBus().get_object( '{{ cookiecutter.dbus_bus_name }}', '{{ cookiecutter.dbus_object_path }}' )
    iface = dbus.Interface( obj, dbus_interface = '{{ cookiecutter.dbus_interface }}' )
    return iface



def test_foo( foo_service ):
    assert foo_service.Foo() == 42



def test_runs_as_patient():
    assert pwd.getpwuid( os.getuid() ).pw_name == 'patient'

