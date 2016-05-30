from setuptools import setup

setup(
    name="ExomiserApi",
    version="0.1",
    install_requires=[
        "flask == 0.10.1",
        "flask-restful == 0.3.5",
        "Flask-CAS == 1.0.0",
        "Flask-Cors == 2.1.2",
        "requests == 2.9.1",
        "gunicorn == 19.4.5",
        "gevent == 1.1rc5",
    ],
    # ...
)
