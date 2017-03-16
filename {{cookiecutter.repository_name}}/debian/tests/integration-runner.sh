#! /bin/bash

set -e
set -x

function service_is_running() {
	systemctl is-active '{{ cookiecutter.systemd_service_name }}.service'
}



function scrape_logs() {
	journalctl >"${ADT_ARTIFACTS}/journal.txt"
}

trap scrape_logs EXIT



if ! service_is_running ; then
	systemctl restart '{{ cookiecutter.systemd_service_name }}.service'

	deadline="$( date +%s )"
	let 'deadline+=60'

	while [[ "$( date +%s )" -le "${deadline}" ]] ; do
		if service_is_running ; then
			break
		else
			sleep 2
		fi
	done

	# let `set -e` bail us out if we exited the loop gracefully instead of via `break`, that is: the deadline expired.
	service_is_running
fi


py.test-3 -ra --cache-clear --junit-xml=$ADT_ARTIFACTS/integration.xml tests/integration

