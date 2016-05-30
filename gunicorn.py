#!/usr/bin/env python
import subprocess

subprocess.call("gunicorn --reload --worker-class gevent --workers 9 -b 0.0.0.0:8082 api:app",shell=True)
