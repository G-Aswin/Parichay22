from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   # return render_template('index.html')
   # return redirect("/events")
   return redirect("/prefest")

@app.route('/prefest')
def prefest():
   return render_template('prefest.html')

# @app.route('/events')
# def events():
#    return redirect("https://drive.google.com/file/d/1pe8VSO1KZaiY-mx959LKLnhtJULHw0sc/view")

@app.route('/events')
def events():
   print('Request for events page received')
   return render_template('events.html')

# @app.route('/events')
# def landingpage():
#    return render_template('events.html')

if __name__ == '__main__':
   app.run()