
\_template
==========

The `_template` repository provides a set of templates for use with `cookiecutter`
(https://cookiecutter.readthedocs.io/en/latest/index.html).


python-library
==============

The python library branch provides a simple python library with the following features:

* it's a python library, you can import it
* it's namespaced under the `gwn` import path
* it comes out of the box with unit tests

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

