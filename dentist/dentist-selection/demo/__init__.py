# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Flask

from . import v1
from .v1.model import init_db


def create_app():
    app = Flask(__name__, static_folder='static')
    init_db()
    app.register_blueprint(
        v1.bp,
        url_prefix='/v1')
    return app


if __name__ == '__main__':
    create_app().run(debug=True)