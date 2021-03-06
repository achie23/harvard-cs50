import csv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = 'postgresql://postgres:2326@localhost:5432/lecture3'
engine = create_engine(DATABASE_URL)
# engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    file = open("flights.csv")
    reader = csv.reader(file)
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",
                    {"origin": origin, "destination": destination, "duration": duration})
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()

if __name__ == "__main__":
    main()
