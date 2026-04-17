import flask
import os

app = flask.Flask(__name__)

@app.route("/")

def hello_world():

    return "Hello, World!"

@app.route("/welcome")

def welcome():

    return "Welcome to the world of GCP and Python!"

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    