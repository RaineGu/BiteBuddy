from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    greeting = "Hello there, Ace"
    return render_template("index.html", greet=greeting)


app.run(debug=True)
