# flask is basically used for creating websites and APis

# Explore the ‘Flask’ module and create a web server using Flask & Python.

import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()