#!/usr/bin/env python
import json
import os
import time
from flask import render_template,request,make_response
from flask_restful import Resource


class rec_json(Resource):
 
  def post(self,uuid):
     f=open(uuid,"w")
     f.write(request.data)
     f.close()

     return uuid    
      
class rec_vcf(Resource):
 
  def post(self,uuid):
     f=open(uuid,"w")
     f.write(request.data)
     f.close()

     return uuid   

      
class run_exo(Resource):
 
  def get(self):

    headers = {'Content-Type': 'text/html'}

    json_file=request.args.get("json")
    vcf_file=request.args.get("vcf")

    hpo=""
    
    with open(json_file) as data_file:    
         data = json.load(data_file)

    for i in range(len(data["features"])):
         hpo += data["features"][i]["id"]+","

    hpo_terms=hpo[:-1]    
    
    
    os.system("java -jar /home/tasos/Downloads/exomiser-cli-7.2.1/exomiser-cli-7.2.1.jar --prioritiser=phive -I AD -F 1 --hpo-ids " + hpo_terms + " -v" + vcf_file)
    time.sleep(2)

    os.system("cp results/" + vcf_file + "-exomiser-results.html templates/")
    #os.system("rm " + json_file)
    #os.system("rm " + vcf_file)


    return make_response(render_template(vcf_file +"-exomiser-results.html"),200,headers)
    #return render_template(vcf_file +"-exomiser-results.html")


 

