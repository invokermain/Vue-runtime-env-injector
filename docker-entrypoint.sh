#!/bin/sh
set -e

# activate our virtual environment here
. /opt/pysetup/.venv/bin/activate

exec "$@"