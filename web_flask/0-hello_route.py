#!/usr/bin/python3
"""
Minimal Flask Application
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """This is the index page of
    the minimal flask application"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
