#!/usr/bin/env python
import json
import subprocess
import ruamel.yaml
from flask import request
from flask_restful import Resource
from flask.ext.cas import login_required


class run_exo(Resource):
 
  #POST method where the vcf and the json file are sent simultaneously and consequentlty Exomiser is running
  #@login_required
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
    hpo_list=[]
    
    with open(json_file) as data_file:    
         data = json.load(data_file)
    
    if "features" in data:
      for i in range(len(data["features"])):
         if data["features"][i]["id"][0:2] == "HP":
            hpo += data["features"][i]["id"]+","
            hpo_list.append(data["features"][i]["id"])

      hpo_terms=hpo[:-1]


    else:
      hpo_terms = "HP:0000001"    
    
 
    '''Run Exomiser with command line parameters'''
    #subprocess.call("java -Xms2g -Xmx4g -jar /home/tasos/Downloads/exomiser-cli-7.2.1/exomiser-cli-7.2.1.jar --prioritiser=" + prior + " -I " + inh + " --hpo-ids " + hpo_terms + " -v" + vcf_file, shell=True)
    #subprocess.call("cp results/" + vcf_file +"-exomiser-results.html /home/tasos/Desktop/rd-connect-client/temp/rd-connect-local-client-0.7.1/local/public/", shell=True)

    #subprocess.call("rm " + vcf_file, shell=True)
    #subprocess.call("rm " + json_file, shell=True)
    #subprocess.call("rm results/" +  vcf_file + "-exomiser-results.html", shell=True)

    '''Run Exomiser with yml template file in order to differentiate between Genomiser and Exomiser'''
    #Read the template for Exomiser
    file_name = 'test-analysis-exome.yml'
    from ruamel.yaml.util import load_yaml_guess_indent

    config, ind, bsi = load_yaml_guess_indent(open(file_name))
    
    #Replace values in the yml dynamically taken by the platform
    analysis = config['analysis']
    analysis['vcf'] = vcf_file
    analysis['hpoIds'] = hpo_list
    
    #Get the vcf basename without the vcf extension
    vcf_base=vcf_file.split('.')[0]
    yml_file = vcf_base + ".yml"


    if inheritance == "UNINITIALIZED" :
      analysis['modeOfInheritance'] = "UNDEFINED"

    else:
      analysis['modeOfInheritance'] = inheritance


    output = config['outputOptions']
    output['outputPrefix']= 'results/' + vcf_base + '-exomiser-results'

    if prioritiser == "PHENIX_PRIORITY":
      del analysis['steps'][-3]
      del analysis['steps'][-2]

    elif prioritiser == "PHIVE_PRIORITY" :
      del analysis['steps'][-3]
      del analysis['steps'][-1]

    elif prioritiser == "HI_PHIVE_PRIORITY" :
      del analysis['steps'][-2]
      del analysis['steps'][-1]


    ruamel.yaml.round_trip_dump(config, open(vcf_base +'.yml', 'w'), 
                            indent=ind, block_seq_indent=bsi)


    subprocess.call("java -Xms2g -Xmx4g -jar /home/tasos/Downloads/exomiser-cli-7.2.1/exomiser-cli-7.2.1.jar --analysis " + yml_file, shell=True)
    subprocess.call("cp results/" +  vcf_base + "-exomiser-results.html /home/tasos/Desktop/rd-connect-client/temp/rd-connect-local-client-0.7.1/local/public/", shell=True)


    subprocess.call("rm " + vcf_file, shell=True)
    subprocess.call("rm " + json_file, shell=True)
    subprocess.call("rm " + yml_file, shell=True)
    subprocess.call("rm results/" +  vcf_base+ "-exomiser-results.html", shell=True)


    return {"file" : vcf_base + "-exomiser-results.html"}

    
