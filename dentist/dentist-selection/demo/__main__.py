# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pprint import pprint

from . import create_app

app = create_app()
# pprint('Initialising mongodb...')
pprint('Starting flask server...')
app.run(debug=True)
