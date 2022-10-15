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


@app.route("/c/<text>", strict_slashes=False)
def c_prefix(text):
    """ C is fun """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_prefix(text="is_cool"):
    """ Python is fun """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
