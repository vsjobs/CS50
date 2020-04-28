import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
# export DATABASE_URL=postgresql+psycopg2://postgres:@localhost/CS50
engine = create_engine('postgresql+psycopg2://postgres:@localhost/CS50')
db = scoped_session(sessionmaker(bind=engine))


def main():
    flights = db.execute(
        "SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")


if __name__ == "__main__":
    main()
# postgresql+psycopg2: // user: password@hostname/database_name'
