from flask import Flask, render_template

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
def map():
    # Map filtering shenanigans here
    return render_template("map.html")


@app.get("/about_me")
def map():
    # About me shenanigans here
    return render_template("about_me.html")


@app.get("/recipes")
def map():
    # Recipe shenanigans here
    return render_template("recipes.html")


app.run(debug=True)
