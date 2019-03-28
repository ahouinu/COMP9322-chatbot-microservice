# -*- coding: utf-8 -*-
from __future__ import absolute_import

from . import create_app

app = create_app()
app.run(debug=True)
