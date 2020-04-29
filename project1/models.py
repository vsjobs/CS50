from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False, unique=True)
    title = db.Column(db.String, nullable=False)
    author_fullname = db.Column(db.String, nullable=False)
    author_firstname = db.Column(db.String, nullable=True)
    author_middlename = db.Column(db.String, nullable=True)
    author_lastname = db.Column(db.String, nullable=True)
    author_nametitle = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=False)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    userid = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


class Reviews(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(
        "books.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    review_title = db.Column(db.String, nullable=False)
    review = db.Column(db.String, nullable=False)
