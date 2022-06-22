from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import db
# from db import day1events, day2events
from flask import g

app = Flask(__name__)

events  = db.events
# events = db.events.sort({'event_id':1})
# g.events = events.find({})

@app.route('/')
def index():
   print('Request for index page received')
   return redirect("/events")

@app.route('/prefest')
def prefest():
   print('Request for prefest page received')
   return redirect("/events")

@app.route('/events')
def events():
   print('Request for events page received')
@app.route('/score')
def score():
   return render_template('score.html')

@app.route('/admin')
def admin():
   return render_template('admin.html')



   events = db.events
   department = db.department
   winners = db.winners

   event_list = events.find(
      {},
      {
         "_id": 0,
         "event_id": 1,
         "event_name": 1,
         "date": 1,
         "time_begin": 1,
         "time_end": 1,
         "venue": 1,
         "max_points": 1,
         "google_form_link": 1,
         "start_hour" : 1
      },
   )

   day1events = []
   day2events = []

   day1 = datetime(2022, 5, 23, 18, 30)
   day2 = datetime(2022, 5, 24, 18, 30)
   for event in event_list:
      if event["date"] == day1:
         day1events.append(event)
      else:
         day2events.append(event)

   day1events = sorted(day1events, key=lambda d: int(d['start_hour'])) 
   day2events = sorted(day2events, key=lambda d: int(d['start_hour'])) 



   return render_template('events.html', d1 = day1events, d2 = day2events)




if __name__ == '__main__':
   app.run()