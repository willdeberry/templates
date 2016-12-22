#! /bin/bash

set -e

function service_is_running() {
	sudo -u patient -i systemctl --user is-active '{{ cookiecutter.systemd_service_name }}.service'
}



systemctl restart gwn-seed-patient.service
# It is unclear when `systemctl` is and is not blocking. If the call to seed /home/patient is non-blocking
# then there is a theoretical race condition here where nodm will start running at a point in time when not
# all of the necessary config files are present in /home/patient.
#
# The consequence of this is that strange errors will occur that look like missing configuration files, and
# when the developer digs in to see if the config files are missing, they will be present. If this is the case
# then an intelligent wait loop with a reasonable timeout will need to be implemented to guarantee completion
# of gwn-seed-patient.service
systemctl restart nodm.service



# systemctl definitely doesn't block for nodm.service, because it is a legacy, sysv init script. Thus,
# we need a wait loop here so we don't start running assertions when test bed setup is incomplete.
deadline="$( date +%s )"
let 'deadline+=60'

while [[ "$( date +%s )" -le "${deadline}" ]] ; do
	if service_is_running &>/dev/null ; then
		break
	else
		sleep 0.25
	fi
done

# let `set -e` bail us out if we exited the loop gracefully instead of via `break`, that is: the deadline expired.
service_is_running


# `adt-run` puts us in a copy of the project source tree, somewhere under /tmp inside the VM
# but `sudo -i` will cd to /home/patient, so we'll need to fully qualify the path to tests/integration
staging_directory="$( pwd )"
sudo -u patient -i py.test-3 --junit-xml=$ADT_ARTIFACTS/integration.xml "${staging_directory}"/tests/integration

