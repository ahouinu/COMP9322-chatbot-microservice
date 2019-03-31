# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pprint import pprint

from flask import Flask

from . import v1
from .v1.model import init_db


def create_app():
    print('Initialising mongodb...')
    init_db()
    app = Flask(__name__, static_folder='static')
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app


if __name__ == '__main__':
    print('Starting flask server...')
    create_app().run(debug=False)
