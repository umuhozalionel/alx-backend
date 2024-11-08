#!/usr/bin/env python3
"""
Flask app module with updated get_locale function
"""

from flask import Flask, request, g
from flask_babel import Babel, _
from typing import Union


app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.before_request
def before_request() -> None:
    """
    Set a mock user as a global on flask.g
    """
    g.user = {"name": "guest", "locale": "fr", "timezone": "UTC"}


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match for supported languages.
    """
    # 1. Locale from URL parameters
    url_locale = request.args.get('locale')
    if url_locale and url_locale in app.config['LANGUAGES']:
        return url_locale

    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

    # 3. Locale from request header
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale

    # 4. Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index() -> str:
    """
    Index view.
    """
    return _("Hello, World!")


if __name__ == "__main__":
    app.run()
