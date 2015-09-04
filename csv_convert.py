# Name: Aman Kaushal
# Contact No: +918989673137
# email: kaushalaman02@gmail.com
# IIIT, Gwalior, India

import json
import csv
import glob
import os
with open("response.csv", "w") as file:
	
	fieldnames = ['engagement_id','metered_distance','metered_time','time_deviation','distance_deviation','Faulty']
	writer = csv.DictWriter(file, fieldnames=fieldnames)
	writer.writeheader()
	filename='response.json'
	print filename
	target = open(filename, 'r')
	data=json.load(target)
	for item in data:
		if item['engagement_id'] and item['metered_distance'] and item['metered_time'] and item['time_deviation'] and item['distance_deviation']:
			writer.writerow({'engagement_id':str(item['engagement_id']).encode('utf-8'),'metered_distance':str(item['metered_distance']).encode('utf-8'),\
				'metered_time':str(item['metered_time']).encode('utf-8'),'time_deviation':str(item['time_deviation']).encode('utf-8'),\
				'distance_deviation':str(item['distance_deviation']).encode('utf-8'),'Faulty':str(item['Faulty']).encode('utf-8')})