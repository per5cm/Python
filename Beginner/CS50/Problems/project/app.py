from flask import Flask, render_template, request
from project import main as get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request == "POST":
        city = request.form["cityName"]
        state = request.form["stateName"]
        country = request.form["countryName"]
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)