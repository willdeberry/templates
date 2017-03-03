"""
{{ cookiecutter.debian_package_long_description | wordwrap( wrapstring = '\n' ) }}

DBus Service
------------

:Bus:
    ``system``
:Busname:
    ``{{ cookiecutter.dbus_bus_name }}``
"""

__title__ = '{{ cookiecutter.python_import_path }}'
__version__ = '0.0.1'
__author__ = 'GetWellNetwork'
__author_email__ = 'plc-dev@getwellnetwork.com'
__copyright__ = 'Copyright 2017 GetWellNetwork, Inc., BSD copyright and disclaimer apply'
__description__ = '{{ cookiecutter.debian_package_short_description }}'
__namespace__ = 'gwn'

BUSNAME = '{{ cookiecutter.dbus_bus_name }}'
OBJECTPATH = '{{ cookiecutter.dbus_object_path }}'
INTERFACE = '{{ cookiecutter.dbus_interface }}'

