from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import math

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "Hello there, Ace"
    return render_template("index.html", greet=greeting)


@app.get("/map")
def map():
    # Map shenanigans here
    return render_template("map.html")


@app.post("/map_filter")
def map_filter():
    # Map filtering shenanigans here
    ret_value1 = request.form['current-location']                  #receive filter input data
    ret_value2 = request.form['distance']
    ret_value3 = request.form['food_preference']           #receive filter input data
    
    state_1 = state_2 = state_3 = True
    if ret_value1 == "":
        state_1 = False
    if ret_value2 == "":
        state_2 = False
    if ret_value3 == "":
        state_3 = False
    
    #the main attribute of json file
    json_str_list = ["name","events"]
    json_event_list = ["time","food"]
    
    json_source = open('data/food_banks.json')      #read json file
    json = json.load(json_source)                   #load json structure
              
    filter_retvalue = []     
         
    for index in json:                              #search in json file
        each_tuple = json[index]                    #get each tuple  
        next_events = []
        next_food = []
        if state_1 :
            app = Nominatim(user_agent="BiteBuddy", timeout=4)
            current_location = app.geocode(ret_value1)
            current_lat = float(current_location.latitude)
            current_long = float(current_location.longitude)
            dst_lat = float(each_tuple["location"].split(","))
            dst_long = float(each_tuple["location"].split(","))
            if math.acos(math.sin(current_lat)*math.sin(dst_lat)+math.cos(current_lat)*math.cos(dst_lat)*math.cos(dst_long-current_long))*6371 < 10000:#within 10km
                if state_3:             #user have diet!!!
                    return 0
                else:                   #user doesn't have diet!!
                    next_food = each_tuple["events"]["food"]

                next_events.append(
                    {
                        "time": each_tuple["events"]["time"],
                        "notes": each_tuple["events"]["notes"],
                        "food": next_food,
                    }
                )
                    
        filter_retvalue.append(
            {
                "id": each_tuple["id"],
                "name": each_tuple["name"],
                "location": each_tuple["location"].split(","),
                "intro": each_tuple["intro"],
                "website":each_tuple["website"],
                "events": next_events,
            }
        )    
        
    return render_template("map.html",banks=filter_retvalue)

@app.get("/about_me")
def about_me():
    # About me shenanigans here
    return render_template("about_me.html")


@app.get("/recipes")
def recipes():
    # Recipe shenanigans here
    return render_template("recipes.html")


if __name__ == '__main__':
    app.run(debug=True)