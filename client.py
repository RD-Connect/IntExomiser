#!/usr/bin/python
import requests

user=0
user+=1

url1 = 'http://127.0.0.1:5000/api/json/hpo1' 
url2 = 'http://127.0.0.1:5000/api/vcf/sample1'
url3 = 'http://127.0.0.1:5000/api/exomiser?json=hpo1&vcf=sample1'


headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}

r1 = requests.post(url1, data=open('phenotips2.json', 'rb'), headers=headers)
r2 = requests.post(url2, data=open('Pfeiffer.vcf', 'rb'))

g=requests.get(url3)

print r1.text
#print r1.headers['content-type']



