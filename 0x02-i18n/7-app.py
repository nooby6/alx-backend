#!/usr/bin/env python3
"""
Flask app with prioritized locale and timezone selection.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)

class Config:
    """
    Configuration for Flask app.
    
    Attributes:
        LANGUAGES (list): Supported languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default language.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)
babel = Babel(app)

# Mock database of users
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id: int) -> Optional[Dict]:
    """
    Retrieve a user dictionary by ID.
    
    Args:
        user_id (int): User ID.
        
    Returns:
        dict or None: User dictionary or None if not found.
    """
    return users.get(user_id)

@app.before_request
def before_request():
    """
    Execute before each request to set a user if logged in.
    Sets g.user to the user object if login_as parameter is provided.
    """
    user_id = request.args.get('login_as', type=int)
    g.user = get_user(user_id)

@babel.localeselector
def get_locale():
    """
    Determines the best matching language for the user, based on:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.get('user') and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
        @babel.timezoneselector
        def get_timezone():
            """
            Determines the best matching timezone for the user, based on:
            1. Timezone from URL parameters
            2. Timezone from user settings
            3. Default to UTC
            """
            timezone = request.args.get('timezone')
            if timezone:
                try:
                    pytz.timezone(timezone)
                    return timezone
                except UnknownTimeZoneError:
                    pass
            if g.get('user') and g.user.get('timezone'):
                try:
                    pytz.timezone(g.user['timezone'])
                    return g.user['timezone']
                except UnknownTimeZoneError:
                    pass
            return app.config['BABEL_DEFAULT_TIMEZONE']