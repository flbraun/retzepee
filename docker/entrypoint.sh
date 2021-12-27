#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

postgres_ready() {
  python << PG_END
import sys

from psycopg2 import connect
from psycopg2.errors import OperationalError

try:
    connect(
        dbname="${POSTGRES_DB}",
        user="${POSTGRES_USER}",
        password="${POSTGRES_PASSWORD}",
        host="${POSTGRES_HOST}",
        port="${POSTGRES_PORT:-5432}",
    )
except OperationalError:
    sys.exit(-1)
PG_END
}

until postgres_ready; do
  >&2 echo "Waiting for PostgreSQL to accept connections..."
  sleep 3
done
>&2 echo "Connected to PostgreSQL"

python manage.py check
python manage.py compilemessages
python manage.py collectstatic --noinput --clear
python manage.py migrate

exec "$@"
