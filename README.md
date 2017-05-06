
\_template
==========

The `_template` repository provides a set of templates for use with `cookiecutter`
(https://cookiecutter.readthedocs.io/en/latest/index.html).


python-dbus-service
===================

The python dbus service branch provides a service process with the following
features:

* long running service
* integrated with systemd for init
* publishes a service on dbus
* it comes out of the box with unit and integration tests

This branch provides:

* debian packaging boilerplate; the following make targets will work:
	* `apt-silo`
	* `tag`
	* `deb`
	* `installnow`
	* `graph`
	* `unit`
* importable python modules
* unit tests
* sphinx API docs published by jenkins builds

