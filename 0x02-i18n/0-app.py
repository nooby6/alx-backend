#!/usr/bin/env python3
"""
This module initializes a basic Flask application with one route.

The app renders a simple HTML template with a welcome message.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Route to render the homepage with a welcome message.
    
    Returns:
        Rendered HTML template for the homepage.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
