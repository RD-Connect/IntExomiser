# IntExomiser 

## Setup

```
./develop.sh              #Create a virtual environment and install all dependencies there
source venv/bin/activate  #Enter the virtualenv
./gunicorn.py             #Start the server
```

## Utility

The client from the genomics platform sends a vcf file together with a json file for a specific donor that queries from the Phenotips database.Parameters like Exomiser algorithm and mode of inheritance are also sent to the service.
The Exomiser web service receives the two files,parses the json in order to get the HPO terms and runs
Exomiser algorithm with inputs the vcf file,the hpo terms,the corresponding exomiser algorithm and the mode of inheritance. 

It stores the results in the "results" folder and returns the Exomiser results back to the genomics platform.

