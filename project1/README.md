# Project 1

Web Programming with Python and JavaScript

Look at querying book table using SQLAlchemy
application.py -  booksearch() method

books = Book.query.filter(
            and_ (Book.isbn.like("%{isbn}%"),
                                       Book.title.like("%{title}%"),
                                       Book.author_fullname.like("%{author}%") )).all()

