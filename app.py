from flask import Flask, render_template
import json
from geopy.geocoders import Nominatim
import time
from pprint import pprint

app = Flask(__name__)


@app.route("/")
def index():
    greeting = "Hello there, Ace"
    return render_template("index.html", greet=greeting)


@app.get("/map")
def map():
    # Retrieving data
    json_file = open("data/food_banks.json")
    data = json.load(json_file)

    # Creating array of food banks
    banks = []
    for bank in data:
        banks.append(
            {
                "id": bank["id"],
                "name": bank["name"],
                "location": bank["location"].split(","),
            }
        )

    # Getting base device postcode to center map
    # Instantiate a new Nominatim client
    app = Nominatim(user_agent="BiteBuddy", timeout=3)
    # Get location raw data
    location = app.geocode("The University of New South Wales")
    lat = float(location.latitude)
    long = float(location.longitude)
    # print(f"lat is ${lat}, long is ${long}")
    print(f"banks is {banks}")
    return render_template("map.html", banks=banks, lat=lat, long=long)


@app.post("/map_filter")
def map_filter():
    # Map filtering shenanigans here
    return render_template("map.html")


@app.get("/about_me")
def about_me():
    # About me shenanigans here
    return render_template("about_me.html")


@app.get("/recipes")
def recipes():
    # Recipe shenanigans here
    return render_template("recipes.html")


app.run(debug=True)
