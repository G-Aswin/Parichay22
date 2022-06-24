from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import db
import scoreboard
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

@app.route('/admin_control')
def admin_route():
   print("reached admin")

   return '<h1> Admin Page </h1>'

@app.route('/admin_control/score')
def score():
   print("reached score")
   db.update_winner()
   return '<h1> score updated </h1>'

@app.route("/scoreboard")
def scoreboard_display():
   return '<h1> scoreboard </h1>'

@app.route("/refresh")
def refresh_scoreboard():
   # file1 = open("winner.txt","r+")
   # win_count = file1.read()
   # if scoreboard.winner_count() > int(win_count):
   #    file1.write(scoreboard.winner_count())
   #    scoreboard.update_score()

   return '<h1>updated scoreboard</h1>'

@app.route('/events')
def events():
   print('Request for events page received')
   return render_template('events.html')
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