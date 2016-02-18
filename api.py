#!/usr/bin/env python
from flask import Flask
from flask.ext.cors import CORS
from flask_restful import Resource, Api
from app.models.server import run_exo

# initialization
app = Flask(__name__)
CORS(app)
api = Api(app,catch_all_404s=True)

api.add_resource(run_exo, '/exomiser')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8082, debug=True)
