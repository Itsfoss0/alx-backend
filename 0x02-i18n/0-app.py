#!/usr/bin/env python3

"""
This module holds a simple module to
learn and practice i18n in flask
"""

from flask import Flask,  render_template
from flask_babel import Babel

class Config:
    """
    Configure the babel object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
babel = Babel(app)

app.config.from_object(Config)
babel.init_app(app)


@app.route("/", strict_slashes=False)
def hello_holberton():
    """
    A simple function that returns
    Hello world from a flask template
    Args:
        None
    Returns:
        Returns a flask template
    ____________________________
    Example
        hello_hoberton()
    """""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
