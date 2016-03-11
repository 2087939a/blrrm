import json
import pandas as pd
import io, json
import csv

listOfIds = []
id = 0

addedList = list()

df = pd.read_csv('videos_sorted.csv', sep = ';')

columns = ['Artist','Location']

tempD = dict()
for c in columns:
	for name in df[c]:
		
		if name not in addedList:
				tempD = {'id':id,'name':name}
				addedList+=[name]
				listOfIds+=[tempD]
				id+=1
				
with open('ids.txt', 'w') as f:
	f.write(json.dumps(listOfIds))


videos = csv.DictReader(open("videos_sorted.csv"), delimiter = ';')



with open('ids.txt', 'r') as f:
	nodes = json.load(f)


links = []
names = []
for row in videos:
	artist = row['Artist']
	location = row['Location']
	sourceArtistId = 0
	targetLocId = 0
	for node in nodes:
		if artist==node['name'].encode('utf-8'):
			sourceArtistId = node['id']
		elif location==node['name'].encode('utf-8'):
			targetLocId = node['id']
	names.append([artist,location])
	links.append({'source':sourceArtistId,'target':targetLocId})

with open('links.txt', 'w') as f:
	f.write(json.dumps(links))



