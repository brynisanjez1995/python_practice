import csv
import json

json_array = []
with open('files\\usa_cities.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        json_array.append(row)

with open('files\\usa_cities.json', 'w') as json_file:
    json_string = json.dumps(json_array, indent=4)
    json_file.write(json_string)



