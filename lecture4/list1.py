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
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == "__main__":
    with app.app_context():
        main()
