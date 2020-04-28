from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/david")
def david():
    return "Hello, David!"


@app.route("/dog")
def dogs():
    return "The list of dogs not rule"
