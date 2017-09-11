import csv
import json
import urllib2
import requests


f = open('data.csv', 'rU')
jsonfile = open('file.json', 'w')
# reader = csv.reader(f )
reader = csv.DictReader(f, fieldnames = ("id","name","dept"))

url='http://dohqdlab01:8083/employees'


headers = {"Content-Type":"application/json","Accept":"application/json"}
for row in reader:
	response = requests.post(url,  headers=headers ,data=json.dumps(row))
if response.status_code != 200:
    print('Status:', response.status_code, 'Headers:', response.headers)
    exit()
