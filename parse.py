# Name: Aman Kaushal
# Contact No: +918989673137
# email: kaushalaman02@gmail.com
# IIIT, Gwalior, India

from __future__ import division
import urllib2
import json
import requests
import math
	
def fault_check(t,time,d,dis):
	if abs(float(t)-float(time)) > 10 and abs(float(d)-float(dis))>2:
		return "YES"
	else:
		return "NO"

base_endpoint = "https://www.test.jugnoo.in:8300/fetch_data" 
try:
	content = urllib2.urlopen(base_endpoint)
except Exception as e: 
	print "Error",e
data = json.loads(content.read())

api_keys = ["AIzaSyDLrGf_YVWO1GfbKnz7CmH0rRAsY7zkMN4", "AIzaSyDYsMoTUO4bBL_NiCwTwNikd2Bk1HlV1y8", \
"AIzaSyD137uAUcurfckhg7dHLXCu0UUXZkOdHoU", "AIzaSyAJhhZGaZpbTzT3_HkzVUzMiW-2tBB6jMY", \
"AIzaSyC4ewZL7bZ8LazvIiQ_g7NgjNbV_VNZ588", "AIzaSyAVNMeEV5qm8BbU5H7Wzddwk48EnuGKKWo", \
"AIzaSyCmUVt3klaEVr8p2KdFupY_2dLURdkNtaM", "AIzaSyBgR5WoBaJI1nDzcb993Rcf02pV4Ov8i1E", \
"AIzaSyAwQfvn1qg8gD8Z8DBZDRPI9Mfe3wiWl4E", "AIzaSyAin9f7BPM7pqqiKkkvRmtBOkvn_Oitlzk"]

l=list()
break_point=10;
k=0
cutoff=len(data)//break_point

for j in range(break_point):
	for i in range(k,cutoff):

		# latitude and longitude for source location
		lat1=data[i]['pickup_latitude']
		long1=data[i]['pickup_longitude']

		# latitude and longitude for destination location 
		lat2=data[i]['drop_latitude']
		long2=data[i]['drop_longitude']
		
		# Google Distance Matrix API url
		url="https://maps.googleapis.com/maps/api/distancematrix/json?origins="\
		+str(lat1)+","+str(long1)+"&destinations="+str(lat2)+","+str(long2)+"&key="+api_keys[j]
				 
		try:
			content=urllib2.urlopen(url) 
		except Exception as e:
			print "Error",e

		data2=json.loads(content.read())

		# Actual Distance Measure given by jugnoo API
		dis=data[i]['metered_distance']

		# Actual Time Measure given by jugnoo API
		time=data[i]['metered_time']

		# Distance and Times measures by Google MAP Api
		d= data2['rows'][0]['elements'][0]['distance']['text'].strip('km')
		t=data2['rows'][0]['elements'][0]['duration']['text'].strip('mins')

		# Calculating Deviations
		if (not dis) or (not time):
			if (not dis) and (not time):
				distance_deviation=abs(float(d)-float(dis))
				time_deviation=abs(float(t)-float(time))
			elif not time:
				time_deviation=abs(float(t)-float(time))
				distance_deviation=(abs(float(d)-float(dis))/float(dis))*100
			elif not dis:
				distance_deviation=abs(float(d)-float(dis))
				time_deviation=(abs(float(t)-float(time))/float(time))*100

		else:
			distance_deviation=(abs(float(d)-float(dis))/float(dis))*100
			time_deviation=(abs(float(t)-float(time))/float(time))*100

		dictionary=dict()
		dictionary["engagement_id"]=data[i]["engagement_id"]
		dictionary["metered_distance"]=data[i]["metered_distance"]
		dictionary["metered_time"]	= data[i]["metered_time"]
		dictionary["time_deviation"]="%.2f"%time_deviation+"%"
		dictionary["distance_deviation"]="%.2f"%distance_deviation+"%"
		dictionary["Faulty"]=fault_check(t,time,d,dis)
		l.append(dictionary)

	k+=(len(data)//break_point)
	cutoff+=(len(data)//break_point)

# Dump all response json data in response.json file created in the same directory
with open('response.json', 'w') as fp:
    json.dump(l, fp)