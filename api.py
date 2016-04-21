#!/usr/bin/env python
from flask import Flask
from flask.ext.cors import CORS
from flask.ext.cas import CAS
from flask_restful import Resource, Api
from app.models.server import run_exo

# initialization
app = Flask(__name__)
CORS(app)
CAS(app)
api = Api(app,catch_all_404s=True)

app.config['CAS_SERVER'] = 'https://platform.rd-connect.eu/cas/login' 
app.config['CAS_AFTER_LOGIN'] = 'get' 
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'

api.add_resource(run_exo, '/exomiser')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8082, debug=True , threaded = True)
