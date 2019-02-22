import os

import csv

  # same import and setup statements as above

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://localhost') # database engine object from SQLAlchemy that manages connections to the database
                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))    # create a 'scoped session' that ensures different users' interactions with the
                                                    # database are kept separate
def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall() # execute this SQL command and return all of the resultsfor flight in flights
    print(f"{flights.origin} to {flights.destination}, {flights.duration} minutes.") # for every flight, print out the flight info
    #print(flights)

if __name__ == "__main__":
    main()
