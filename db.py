import collections
from sqlite3 import Date
from flask_pymongo import pymongo
from datetime import datetime

client = pymongo.MongoClient(
    "mongodb+srv://cat-rnsit:parichay2022@cluster0.cwu4w3u.mongodb.net/?retryWrites=true&w=majority"
)
db = client.get_database("parichay")

events = db.events
department = db.department
winners = db.winners

# """command for printing all the document within event"""

# event_list_all = events.find({})
# for event in event_list_all:
# 	print(event,end="\n\n")


# printing list of events with their respective date

# event_list = events.find(
#     {},
#     {
#         "_id": 0,
#         "event_id": 1,
#         "event_name": 1,
#         "date": 1,
#         "time_begin": 1,
#         "time_end": 1,
#         "venue": 1,
#         "max_points": 1,
#         "google_form_link": 1,
#     },
# )

# day1events = []
# day2events = []

# day1 = datetime(2022, 5, 23, 18, 30)
# day2 = datetime(2022, 5, 24, 18, 30)
# for event in event_list:
#     # print(f"{event['event_name']} is on {event['date']}")
#     # e_l.append(f" {event['event_id']}   {event['event_name']} is on {event['date']}")
#     if event["date"] == day1:
#         day1events.append(event)
#     else:
#         day2events.append(event)

# day1events = sorted(day1events, key=lambda d: d['time_begin']) 
# day2events = sorted(day2events, key=lambda d: d['time_begin']) 



# print(len(day1events))
# print(len(day2events))

# print(day1events[0])
# print(day2events[0])


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
