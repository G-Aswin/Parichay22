from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   # return render_template('index.html')
   return redirect("/events")

@app.route('/events')
def landingpage():
   return render_template('events.html')

if __name__ == '__main__':
   app.run()