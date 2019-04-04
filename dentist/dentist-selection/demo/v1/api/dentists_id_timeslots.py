# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import os
from pprint import pprint

import requests
from flask import request, g, jsonify, make_response

from . import Resource
from .. import schemas
from ..model import mongo_driver as db

host_url = os.environ['TIMESLOT_URL']


class DentistsIdTimeslots(Resource):

    def get(self, id):
        dentist = db.get_dentist_by_id(int(id))
        if dentist:
            # url = f'http://localhost:5001/v1/timeslots?doc_id={id}'
            url = f'{host_url}/v1/timeslots?doc_id={id}'
            resp = requests.get(url)
            return resp.json(), resp.status_code, resp.headers.items()
        else:
            return {'message': 'Dentist not found on server'}, 404, None
