#!/usr/bin/python3
""" Hello HBNB """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ hello HBNB route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """ display HBNB route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
