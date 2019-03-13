#!/usr/bin/env bash

CURRENT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "${CURRENT_DIR}/.."
source .venv/bin/activate

cd "${CURRENT_DIR}"
python manage.py migrate
python manage.py creatersakey
python manage.py createsuperuser
