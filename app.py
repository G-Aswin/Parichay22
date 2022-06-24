from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import db
import scoreboard
from collections import defaultdict

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
def score_updated():
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
@app.route('/score')
def score():
   winners = db.winners
   winner_list = winners.find(
         {},
         {
            "_id": 0,
            "dept_id": 1,
            "event_id": 1,
            "position": 1,
            "points_scored": 1,
            "winner_name": 1,
         },
      )

   for winner in winner_list:
      print(winner)

   departments = db.department
   department_list = departments.find(
      {},
      {
         "_id":1,
         "dept_name":1
      },
   )

   # id_to_name = {}
   # for entry in department_list:
   #    id_to_name[entry['_id']] = entry['dept_name']
   winner_list = winners.find(
         {},
         {
            "_id": 0,
            "dept_id": 1,
            "event_id": 1,
            "position": 1,
            "points_scored": 1,
            "winner_name": 1,
         },
      )
   dept_scores = defaultdict(int)
   for winner in winner_list:
      # print(winner)
      dept_scores[winner['dept_id']] += int(winner['points_scored'])

   print(dept_scores)

   score = []
   for entry in department_list:
      score.append([entry['dept_name'], dept_scores[entry['_id']]])
      # print(entry)
   
   print(score)

   score.sort(key=lambda x:x[0], reverse=False)
   score.sort(key=lambda x:x[1], reverse=True)



   return render_template('score.html', dept_points = score)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
   if request.method == 'GET':

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
      dept_list = department.find(
         {},
         {
            "_id": 0,
            "dept_id": 1,
            "dept_name": 1,
         },
      )


      return render_template('admin.html', events = event_list, depart = dept_list)
   else:
      password = request.form.get("password")
      points = request.form.get("points")
      winner_name = request.form.get("winner_name")
      event = request.form.get("event")
      position = request.form.get("position")
      dept = request.form.get("dept")

      print(password, points, winner_name, event, position, dept)

      if password != "asswin":
         return "Fuck off"


      db.update_winner(event, dept, position, points, winner_name)
      return "Winner Updated"






if __name__ == '__main__':
   app.run()