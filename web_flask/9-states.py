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


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_states():
    """ Render all cities by state """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def display_states_v0(id=None):
    """ Render all the states in storage """
    states = storage.all(State)
    if not id:
        return render_template('7-states_list.html', states=states.values())

    key = "State.{}".format(id)
    state = None
    try:
        state = states[key]
    except Exception:
        pass

    return render_template('9-states.html', state=state)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
