#!/usr/bin/env python
import requests,json
import subprocess

#Query the Phenotips Api in order to get the json with the information of the specific patient
phenotips = 'http://localhost:8081/phenotips/ExportPatient?id=P0000002'

json = requests.get(phenotips)
vcf  = open('/home/tasos/Downloads/null_E000010_1460542983123.vcf', 'rb')

#Endpoint of Exomiser service
url = 'http://localhost:8082/exomiser?prioritiser=PHENIX_PRIORITY&inheritance=AUTOSOMAL_DOMINANT'
headers = {'Content-Type' : 'application/text'}

multiple_files = [('files', ('sample.vcf', vcf,  'file/vcf')),
                  ('files', ('donor.json', json.text, 'file/json'))
                 ]

r1 = requests.post(url, files = multiple_files)

print r1.text

#g=requests.get(url)


