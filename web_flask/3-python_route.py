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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB router page"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """Displays c + text
    replacing _s with spaces"""
    text = text.replace('_', ' ')
    return 'c {}'.format(text)


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """Displays c + text
    replacing _s with spaces"""
    text = text.replace('_', ' ')
    return "C %s" % text


if __name__ == '__main__':
    app.run(host='0.0.0.0')
