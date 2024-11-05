#!/usr/bin/env python3
"""
Flask app with Babel setup to allow language selection via URL parameter.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    Determines the best-matching language for the user, either from the 'locale'
    URL parameter or the Accept-Language headers.
    
    Returns:
        str: The best-matching language code.
    """
    # Check if 'locale' is passed in the URL query and is supported
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # Fallback to default behavior based on headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route to render the homepage with a welcome message.
    
    Returns:
        Rendered HTML template for the homepage.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
