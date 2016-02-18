#!/usr/bin/env python
import json
import os
from flask import request
from flask_restful import Resource

class run_exo(Resource):
 
  #POST method where the vcf and the json file are sent simultaneously and consequentlty Exomiser is running
  def post(self):
    
    '''Get the 2 files from the genomics platform and save them locally at server'''
    for file in request.files.getlist("files"):
         filename = file.filename.rsplit('/')[0]
         file.save(filename)
       
    #We get the file names from the request files
    vcf_file  = request.files.getlist("files")[0].filename.rsplit('/')[0]
    json_file = request.files.getlist("files")[1].filename.rsplit('/')[0]
    #params_file = request.files.getlist("files")[2].filename.rsplit('/')[0]

    #We parse the query parameters if we provide them in the url
    prioritiser=request.args.get("prioritiser")
    inheritance=request.args.get("inheritance")
    
    #Mode of inheritance handling
    if inheritance == "AUTOSOMAL_DOMINANT" :
       inh = "AD"

    elif inheritance == "AUTOSOMAL_RECESSIVE" :
       inh = "AR"

    elif inheritance == "X_RECESSIVE" :
       inh = "X"

    elif inheritance == "UNINITIALIZED" :
       inh = "U"


    #Prioritizer handling
    if prioritiser == "PHENIX_PRIORITY" :
       prior = "phenix"

    elif prioritiser == "PHIVE_PRIORITY" :
       prior = "phive"

    elif prioritiser == "HI_PHIVE_PRIORITY" :
       prior = "hiphive"

    
    #JSON parsing in order to get the HPO terms
    hpo=""
    
    with open(json_file) as data_file:    
         data = json.load(data_file)
    
    if "features" in data:
      for i in range(len(data["features"])):
         hpo += data["features"][i]["id"]+","

      hpo_terms=hpo[:-1]

    else:
      hpo_terms = "HP:0000001"    
    
    #Exomiser run and return of html output
    os.system("java -jar /home/tasos/Downloads/exomiser-cli-7.2.1/exomiser-cli-7.2.1.jar --prioritiser=" + prior + " -I " + inh + " --hpo-ids " + hpo_terms + " -v" + vcf_file)
    os.system("cp results/" + vcf_file +"-exomiser-results.html /home/tasos/Desktop/rd-connect-client/temp/rd-connect-local-client-0.7.1/local/public/")

    os.system("rm " + vcf_file)
    os.system("rm " + json_file)
    
    return {"file" : vcf_file + "-exomiser-results.html",
            "hpo" : hpo_terms}

    
    #os.system("cp results/sample.vcf-exomiser-results.html templates/")
   
    #return "Exomiser finished"
    #return send_from_directory('html', "results/sample.vcf-exomiser-results.html")
    #return make_response(render_template("sample.vcf-exomiser-results.html"),200,headers)
    #return render_template("sample.vcf-exomiser-results.html")

    