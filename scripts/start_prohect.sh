#!/usr/bin/env bash

set -e -v

rm -rf venv/
virtualenv -p python3.8 venv
source venv/bin/activate
pip install -r requirements.txt
Site/manage.py migrate
Site/manage.py collectstatic
Site/manage.py runserver 8000
