import csv
import os
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
DATABASE_URL = 'postgresql://postgres:2326@localhost:5432/lecture4'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    file = open("flights.csv")
    reader = csv.reader(file)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
