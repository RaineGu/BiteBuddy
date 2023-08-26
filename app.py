from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    greeting = "Hello there, Ace"
    return render_template("index.html", greet=greeting)


@app.get("/map")
def map():
    # Map shenanigans here
    return render_template("map.html")


#@app.route('/map_filter',methods = ['POST', 'GET'])
@app.post("/map_filter")
def map_filter():
    # Map filtering shenanigans here
    
    ret_value1 = request.form['name']                  #receive filter input data
    ret_value2 = request.form['events-time']           #receive filter input data
    ret_value3 = request.form['events-food']           #receive filter input data
    
    #the main attribute of json file
    json_str_list = ["name","events"]
    json_event_list = ["time","food"]
    
    json_source = open('data/food_banks.json')      #read json file
    json = json.load(json_source)                   #load json structure
         
    for index in json:
        each_tuple = json[index]                    #get each tuple
        for x in range(len(json_str_list)):
            if json_str_list[x] != "events":    #it's not event
                if each_tuple["name"] == ret_value1:
                    return 0                
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
                pass         
        pass
    pass
    return render_template("map.html")


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