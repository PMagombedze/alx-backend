#!/usr/bin/env python3


"""Pybabel"""


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """home page"""
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run()
