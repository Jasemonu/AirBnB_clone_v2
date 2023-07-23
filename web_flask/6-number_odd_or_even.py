#!/usr/bin/python3
"""
A script that starts a Flask web application:
The web application listens on 0.0.0.0, port 5000
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
"""
from flask import Flask, render_template

app = Flask(__name__)


# Route for '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def display_text(text):
    # Replace underscore with a space in the text
    text = text.replace('_', ' ')
    return f'C {text}'


# Route for '/python/(<text>)'
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    # Replace underscore with a space in the text
    text = text.replace('_', ' ')
    return f'Python {text}'


# Route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f'{n} is a number'


# Route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)


# Route for '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
