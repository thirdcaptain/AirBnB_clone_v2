#!/usr/bin/python3
"""Flask web app that prints Hello HBNB!"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """shows c and text"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", defaults={"text": "is cool"})
@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python_text(text):
    """shows python and text"""
    text = text.replace("_", " ")
    return "Python %s" % text

if __name__ == '__main__':
    app.run()
