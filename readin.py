import json

#Opening JSON file
j = open('Data.json')

#returns JSON as a dictionary
data = json.load(j)

#Iterating through the json list
for i in data['project']:
	print(i)

#closing file
j.close()
