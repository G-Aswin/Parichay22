from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import db
from flask import g

app = Flask(__name__)

events  = db.events
# events = db.events.sort({'event_id':1})
# g.events = events.find({})

@app.route('/')
def index():
   print('Request for index page received')
   return redirect("/prefest")

@app.route('/prefest')
def prefest():
   return render_template('prefest.html')


@app.route('/events')
def events():
   print('Request for events page received')
   return render_template('events.html')




if __name__ == '__main__':
   app.run()