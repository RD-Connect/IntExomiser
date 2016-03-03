#!/usr/bin/env python
import subprocess

subprocess.call("gunicorn --reload --worker-class gevent --workers 9 -b localhost:8082 api:app",shell=True)
