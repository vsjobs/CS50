import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    yesMsg = "Yes It's New Year"
    noMsg = "No it's not new year"
    new_year = now.month == 1 and now.day == 1
    return render_template("index.html", new_year=new_year, yesMsg=yesMsg, noMsg=noMsg)


@app.route("/birthday")
def birthday():
    now = datetime.datetime.now()
    new_year = now.month == 4 and now.day == 20
    yesMsg = "Yes It's Your Birthday"
    noMsg = "No it's not your birthday"
    return render_template("index.html", new_year=new_year, yesMsg=yesMsg, noMsg=noMsg)
