from flask_pymongo import pymongo

client = pymongo.MongoClient("mongodb+srv://cat-rnsit:parichay2022@cluster0.cwu4w3u.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('parichay')

""" 
Parichay

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

events = db.events
department = db.department
winners = db.winners

"""next task is to add the json document in these databases  in the same order given above""" 

print(events.count_documents({}))
