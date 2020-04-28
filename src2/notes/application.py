from flask import Flask, render_template, request, session
from flask_session import Session


app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
sess = Session()
sess.init_app(app)
# Session(app)

notes = []


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") == None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        # notes.append(note)
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])
