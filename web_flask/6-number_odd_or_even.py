#!/usr/bin/python3
"""
Minimal Flask Application
"""

from flask import Flask, render_template
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
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def py_text(text='is cool'):
    """python + variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display n if integer"""
    return "%i is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """introducing Jinja templates"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_even_odd(n):
    """odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
