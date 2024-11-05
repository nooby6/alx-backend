#!/usr/bin/env python3
"""
This module initializes a Flask application with Babel for internationalization.

The app is configured to support English and French languages.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Flask app settings.
    
    Attributes:
        LANGUAGES (list): List of supported languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default locale set to English ('en').
        BABEL_DEFAULT_TIMEZONE (str): Default timezone set to UTC.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Route to render the homepage with a welcome message.
    
    Returns:
        Rendered HTML template for the homepage.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
