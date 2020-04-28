from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        name = "Vanishree Viswanath"
    else:
        name = request.form.get("name")
    return render_template("hello.html", name=name)


@app.route("/hello1", methods=["GET"])
def hello1():
    name = "Vanishree"
    name = name.capitalize()
    return render_template("hello.html", name=name)
