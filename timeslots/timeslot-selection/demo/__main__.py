# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pprint import pprint

from . import create_app
from .v1.model import init_db

app = create_app()
pprint('Initialising mongodb...')
init_db()
pprint('Starting flask server...')
app.run(debug=True)
