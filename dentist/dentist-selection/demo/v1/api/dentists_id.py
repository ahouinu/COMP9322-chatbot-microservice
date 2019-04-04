# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from pprint import pprint

from flask import request, g, jsonify, make_response

from . import Resource
from .. import schemas
from ..model import mongo_driver as db


class DentistsId(Resource):

    def get(self, id:int):
        dentist = db.get_dentist_by_id(int(id))
        if dentist:
            resp = make_response(jsonify(dentist))
            return resp
        else:
            return {'message': 'Dentist not found on server'}, 404, None