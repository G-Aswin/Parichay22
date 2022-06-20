from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_pymongo import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://cat-rnsit:parichay2022@cluster0.cwu4w3u.mongodb.net/?retryWrites=true&w=majority")
db = client.test

@app.route('/')
def index():
   print('Request for index page received')
   # return render_template('index.html')
   return redirect("/prefest")

@app.route('/prefest')
def prefest():
   return render_template('prefest.html')

@app.route('/events')
def events():
   return redirect("https://drive.google.com/file/d/1pe8VSO1KZaiY-mx959LKLnhtJULHw0sc/view")

# @app.route('/events')
# def events():
#    print('Request for events page received')
#    return render_template('events.html')


if __name__ == '__main__':
   app.run()