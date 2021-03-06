# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask import Blueprint, redirect, url_for
import flask_restful as restful

from .routes import routes
from .validators import security


@security.scopes_loader
def current_scopes():
    return []

bp = Blueprint('v1', __name__, static_folder='static')
api = restful.Api(bp, catch_all_404s=True)

for route in routes:
    api.add_resource(route.pop('resource'), *route.pop('urls'), **route)


@bp.route('/help')
def show_swagger():
    return redirect(url_for('static', filename='swagger-ui/index.html'))
