import csv
import json
import urllib2

csvfile = open('data.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("id","name","dept")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    req = urllib2.Request('http://dohqdlab01:8083/employees/json.dump(row)')
    req.add_header('Content-Type', 'application/json')

    response = urllib2.urlopen(req)

