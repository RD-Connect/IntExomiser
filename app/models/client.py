#!/usr/bin/env python
import requests,json

#Query the Phenotips Api in order to get the json with the information of the specific patient
phenotips = 'http://localhost:8081/phenotips/ExportPatient?id=donor001'

url1 = 'http://localhost:8082/exomiser/json/json1' 
url2 = 'http://localhost:8082/exomiser/vcf/sample1'
url3 = 'http://localhost:8082/exomiser/exomiser?json=json1&vcf=sample1'

headers = {'Content-Type' : 'application/json'}

patient = requests.get(phenotips)

#print patient.text

#r1 = requests.post(url1, data=open('/home/tasos/Desktop/Exomiser_Api/phenotips2.json', 'rb'))
r1 = requests.post(url1, data=patient.text)
r2 = requests.post(url2, data=open('/home/tasos/Desktop/Exomiser_Api/Pfeiffer.vcf', 'rb'))

g=requests.get(url3)

