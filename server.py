#!/usr/bin/python
import json
import os
import time
import commands
from flask import Flask, render_template, send_from_directory , request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/api/json/<uuid>', methods=['POST'])
def rec_json(uuid):
    
    f=open(uuid,"w")
    f.write(request.json)
    f.close()    
    
    
    return "OK"
    

@app.route('/api/vcf/<uuid>', methods=['POST'])
def rec_vcf(uuid):

    f=open(uuid,"w")
    f.write(request.data)
    f.close() 
    
    return uuid

@app.route('/api/exomiser', methods=['GET'])
def run_exo():
    #import ipdb;ipdb.set_trace()

    json_file=request.args.get("json")
    vcf_file=request.args.get("vcf")

    hpo=""
      
    for i in range(len(content["features"])):
         hpo += content["features"][i]["id"]+","

    hpo_terms=hpo[:-1]
    
    #os.system("java -jar exomiser-cli-6.0.0.jar --prioritiser=phive -I AD -F 1 --hpo-ids " + hpo_terms + " -v Pfeiffer23.vcf")
    os.system("ls")
    #time.sleep(4)
    
    return commands.getoutput('xdg-open results/Pfeiffer23-exomiser-6.0.0-results.html')

    return uuid
    
if __name__ == '__main__':
    app.run(debug=True)

