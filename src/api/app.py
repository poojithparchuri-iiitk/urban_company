from flask import Flask

app = Flask(__name__)

@app.route("/forecast", methods=["POST"])
def forecast():
    # Return a 7-day booking forecast for a given city and service
    pass

if __name__ == "__main__":
    app.run(debug=True)