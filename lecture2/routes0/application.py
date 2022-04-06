from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask world!"

@app.route("/brian")
def brian():
    return "Hello, Great man Brian!"

@app.route("/eve")
def eve():
    return "Welcome, Great woman"