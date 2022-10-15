#!/usr/bin/python3
""" HBNB States with flask """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Tears down session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    """ Render all the states in storage """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
