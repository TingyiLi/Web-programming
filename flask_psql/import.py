import os

import csv

  # same import and setup statements as above
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://localhost') # database engine object from SQLAlchemy that manages connections to the database                                                    # DATABASE_URL is an environment variable that indicates where the database lives
db = scoped_session(sessionmaker(bind=engine))    # create a 'scoped session' that ensures different users' interactions with the

def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader: # loop gives each column a name
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES ( :origin, :destination, :duration)",
                    {"origin": origin, "destination": destination, "duration": duration}) # substitute values from CSV line into SQL command, as per this dict
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes." )
    db.commit() # transactions are assumed, so close the transaction finished

if __name__ == "__main__":
    main()# database are kept separate
