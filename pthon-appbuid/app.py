import flask
import os

app = flask.Flask(__name__)

@app.route("/")

def hello_world():

    return "Hello, World! This is my first Python application deployed on GCP using Cloud Build and Cloud Run. I am excited to learn more about GCP and Python and build more applications in the future."
 
@app.route("/welcome")

def welcome():

    return "Welcome to the world of GCP and Python! and it's running in cloud run"
    

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    