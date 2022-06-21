import collections
from flask_pymongo import pymongo

client = pymongo.MongoClient("mongodb+srv://cat-rnsit:parichay2022@cluster0.cwu4w3u.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('parichay')

events = db.events
department = db.department
winners = db.winners

# """command for printing all the document within event"""

# event_list_all = events.find({})
# for event in event_list_all:
# 	print(event,end="\n\n")


# printing list of events with their respective date

event_list = events.find({},{'_id':0,'event_name':1,'date':1})
e_l = list()
for event in event_list:
	# print(f"{event['event_name']} is on {event['date']}")
	e_l.append(f"{event['event_name']} is on {event['date']}")

for e in e_l:
	print(e)








""" 
Parichay

format of database

events:
	event_id
	date
	time_begin
	time_end
	venue
	event_name
	max_points
	google_form_link
	
department:
	dept_id
	department_name
	logo_img
	
winners:
	dept_id
	event_id
	position(1st, 2nd or 3rd)
	points_scored
   
"""
