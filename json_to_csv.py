import csv
import json

infile = open("files\\usa_cities.json","r")
outfile = open("generated.csv","w", newline='')

writer = csv.writer(outfile)

count = 0
for row in json.load(infile):
    if count == 0:
        writer.writerow(row.keys())
        count += 1
    writer.writerow(row.values())

