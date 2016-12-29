#! /bin/bash

if ! [[ -e ./debian/changelog ]] ; then
	dch --create --package {{ cookiecutter.debian_package_name }} --newversion 0.0.1 'Initial release.'
fi


$EDITOR README.md


cat <<EOF



Awesome!

Here's what to do next:
 1. Go into gitlab
 2. Create a project named '{{ cookiecutter.repository_name }}'
 3. Come back here
 4. Run these commands:
	cd {{ cookiecutter.repository_name }}
	git init
	git add .
	git commit -m 'initial commit'
	git remote add origin git@git.internal.getwellnetwork.com:plcdev/{{ cookiecutter.repository_name }}.git
	git push -u origin master

EOF

