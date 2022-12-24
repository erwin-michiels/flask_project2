from flask import Flask
from flask import request
from flask import render_template
import datetime

flask_image = Flask(__name__)

@flask_image.route("/docs")
def docs():
    return render_template("docs.html" , datetime_now = datetime.datetime.now())

@flask_image.route("/")
def main():
    return render_template("index.html" , datetime_now = datetime.datetime.now())

if __name__ == "__main__":
    flask_image.run(host="0.0.0.0", port=8008)