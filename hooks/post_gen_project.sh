#! /bin/bash

if ! [[ -e ./debian/changelog ]] ; then
	dch --create --package {{ cookiecutter.debian_package_name }} --newversion 0.0.1
fi

