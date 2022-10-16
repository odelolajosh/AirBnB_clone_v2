#!/usr/bin/python3
""" HBNB States with flask """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Tears down session """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """ Hbnb filters """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template(
        '100-hbnb.html', states=states,
        amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
