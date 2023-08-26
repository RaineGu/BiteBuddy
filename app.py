from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import cmath

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
        each_tuple["location"].split(",")
        if state_1 :
            
            app = Nominatim(user_agent="BiteBuddy", timeout=4)
            current_location = app.geocode(ret_value1)
            current_lat = float(current_location.latitude)
            current_long = float(current_location.longitude)
            dst_lat = 1.1
            dst_long = 2.2
            
            if acos(sin(current_lat)*sin(dst_lat)+cos(current_lat)*cos(dst_lat)*cos(dst_long-current_long))*6371 < 10000:                           #within 10km
                
                 
        
        if state_3 :                                    #judge food category
            next_food = each_tuple["events"]["food"]    #get food tuple
            
        
        

        
        
        next_food = []
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
        
        
        
        
        for x in range(len(json_str_list)):
            if json_str_list[x] != "events":        #it's not event
                if each_tuple["name"] == ret_value1:
                        
            elif json_str_list[x] == "events" and ret_value2 == "" and ret_value3 == "":  #it is event but we don't need it
                break
            else:
                event_tuple = each_tuple["events"]
                for event in event_tuple:
                    each_event_tuple = event_tuple[event]
                    for y in range(len(json_event_list)): 
                        #-------------------------------------------#
                        if json_event_list[y] == "time":
                            if each_event_tuple[json_event_list[y]] == ret_value2:
                                return 0
                        else:
                            food_tuple = each_event_tuple[json_event_list[y]]
                            flag = 0
                            for food_index in food_tuple:
                                if food_tuple[food_index] == ret_value3:
                                    flag = 1
                                    break
                            if flag:
                                return 1
                            else:
                                return 1



    return render_template("map.html",banks=filter_retvalue)



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