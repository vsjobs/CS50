import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    isbn = "0345484088"
    qs = "%" + isbn+"%"
    print(qs)
    books = Book.query.filter(Book.isbn.like(qs)).all()
    print(f"Books returned = {books}")


if __name__ == "__main__":
    with app.app_context():
        main()
