#! /bin/bash

set -e

user="$1"
service="$2"

sudo -u "${user}" PAGER=/bin/cat -i dbus-launch bash -c "systemctl --user daemon-reload; systemctl --user start '${service}' || journalctl --user -xe; whoami"
#py.test-3 --junit-xml=$ADT_ARTIFACTS/integration.xml tests/integration

