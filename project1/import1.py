import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    f = open("books.csv")
    reader = csv.reader(f)

    for isbn, title, author_fullname, year in reader:
        try:
            book = Book(isbn=isbn, title=title, author_fullname=author_fullname,
                        year=year)
            db.session.add(book)
            print(
                f"Added book isbn =  {isbn} title = {title} author = {author_fullname} published year = {year}")
        except Exception as e:
            print(
                f"Not adding book isbn =  {isbn} title = {title} author = {author_fullname} published year = {year}")
            continue
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        main()
