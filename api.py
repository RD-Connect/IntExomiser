#!/usr/bin/env python
from flask import Flask
from flask_restful import Resource, Api
from app.models.server import rec_json,rec_vcf,run_exo

# initialization
app = Flask(__name__)
api = Api(app,catch_all_404s=True)

api.add_resource(rec_json, '/exomiser/json/<uuid>')
api.add_resource(rec_vcf, '/exomiser/vcf/<uuid>')
api.add_resource(run_exo, '/exomiser/exomiser')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=8082, debug=True)
