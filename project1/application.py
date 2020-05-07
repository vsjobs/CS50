import os

from flask import Flask, session, render_template, request
import requests
import json

from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


""" @app.route("/")
def index():
    return "Project 1: TODO"
 """


def getGoodReadsRating(isbn):
    key = "YLa1bBC37wdmIYZNJnkBw"
    res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": key, "isbns": isbn})
    book_json = res.json()
    books = book_json["books"]
    book = books[0]
    ratings_count = book['work_ratings_count']
    average_rating = book["average_rating"]

    # book = json.loads(book_json)
    # print(book)
    # b1 = book["books"]
    # rating_count = b1['work_ratings_count']
    # print(b1)
    return ratings_count, average_rating


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        # email = request.form.get("email")
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        password1 = request.form.get("password")
        password2 = request.form.get("password2")
        if password1 == password2:
            user = User(first_name=firstname,
                        last_name=lastname, userid=username, password=password1)
            db.session.add(user)
            db.session.commit()

            msg = "User successfully added"
            return render_template("login.html")

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(
            userid=username, password=password).first()
        if not user:
            return render_template("error.html", message="No such user with that username.")
        else:
            session["user"] = user
            return render_template("booksearch.html")
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    session["user"] = None
    return render_template("index.html")


@app.route("/booksearch", methods=["GET", "POST"])
def booksearch():
    if request.method == "POST":
        isbn = request.form.get("isbn")
        # email = request.form.get("email")
        title = request.form.get("title")
        author = request.form.get("author")
        # Use like query for title and author_fullname
        qs_isbn = "%" + isbn+"%"
        qs_title = "%" + title+"%"
        qs_author = "%" + author+"%"
        books = Book.query.filter(Book.isbn.like(qs_isbn),
                                  Book.title.like(qs_title),
                                  Book.author_fullname.like(qs_author)).all()
        # books = Book.query.filter(Book.isbn.like(qs_isbn)).all()
        # print(f"Books returned = {books}")
        return render_template("booksearch.html", books=books)

        # reviews = Reviews.query.filter_by(book_id=book.id)
        # Return reviews list to the html to display.
    else:
        return render_template("booksearch.html")


@app.route("/review/<int:book_id>", methods=["GET", "POST"])
def review(book_id):
    if request.method == "GET":
        book = Book.query.get(book_id)
        # Good reads to get review and save reviews
        reviews = Reviews.query.filter_by(book_id=book_id)
        rating_count, average_rating = getGoodReadsRating(book.isbn)
        return render_template("review.html", book=book, reviews=reviews,
                               rating_count=rating_count, average_rating=average_rating)
    if request.method == "POST":
        user = session["user"]
        if not user:
            return render_template("error.html", message="No such user with that username.")
        else:
            print(user)
            review_title = request.form.get("review_title")
            review_text = request.form.get("review_text")
            review = Reviews(book_id=book_id,
                             user_id=user.id, review_title=review_title,
                             review=review_text)
            db.session.add(review)
            db.session.commit()
            reviews = Reviews.query.filter_by(book_id=book_id)
            book = Book.query.get(book_id)
            rating_count, average_rating = getGoodReadsRating(book.isbn)

            return render_template("review.html", book=book, reviews=reviews,
                                   rating_count=rating_count, average_rating=average_rating)
