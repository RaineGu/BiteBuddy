from flask import Flask, render_template, request
import json
from geopy.geocoders import Nominatim
from datetime import datetime
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
        # Calculating date of next events (max 3)
        next_events = []
        while len(next_events) < 3 and len(bank["events"]) > len(next_events):
            ts = (
                int(bank["events"][len(next_events)]["time"]) + 36000
            )  # Time zone to AEST
            next_events.append(
                datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %A %H:%M")
            )
            if int(datetime.utcfromtimestamp(ts).strftime("%H")) < 12:
                next_events[len(next_events) - 1] += "AM"
            else:
                next_events[len(next_events) - 1] += "PM"

        # Adding events to pass into website
        banks.append(
            {
                "id": bank["id"],
                "name": bank["name"],
                "location": bank["location"].split(","),
                "intro": bank["intro"],
                "website": bank["website"],
                "events": next_events,
            }
        )

    # Getting base device postcode to center map
    # Instantiate a new Nominatim client
    app = Nominatim(user_agent="BiteBuddy", timeout=4)
    # Get location raw data
    location = app.geocode("The University of New South Wales")
    lat = float(location.latitude)
    long = float(location.longitude)
    return render_template("map.html", banks=banks, lat=lat, long=long)


@app.route("/hub_info")
def hub_info():
    id = request.args.get("hub")
    print(f"id is {id}")

    # Retrieving data
    json_file = open("data/food_banks.json")
    data = json.load(json_file)
    bank = {}

    for data_bank in data:
        print(f"bank is {data_bank}")
        if int(data_bank["id"]) == int(id):
            bank = data_bank
            print(f"bank is {data_bank}")

    if bank == {}:
        return "404 not found D:"

    # Formatting date time for events
    events = []
    for event in bank["events"]:
        ts = int(event["time"]) + 36000  # Time zone to AEST
        time = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %A %H:%M")
        if int(datetime.utcfromtimestamp(ts).strftime("%H")) < 12:
            time += "AM"
        else:
            time += "PM"
        events.append({"time": time, "notes": event["notes"], "food": event["food"]})

    # Populating bank obj
    target_bank = {
        "id": bank["id"],
        "name": bank["name"],
        "location": bank["location"].split(","),
        "intro": bank["intro"],
        "website": bank["website"],
        "events": events,
    }

    return render_template("hub_info.html", bank=target_bank)


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
