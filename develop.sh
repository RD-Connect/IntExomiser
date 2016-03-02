#!/bin/bash
virtualenv venv
source venv/bin/activate
python config/setup.py install
#./gunicorn.py
#./api.py
#
