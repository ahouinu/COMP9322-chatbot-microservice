# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, jsonify, make_response

from . import Resource
from .. import schemas
from ..model import mongo_driver as db


class Dentists(Resource):

    def get(self):
        _list = [_ for _ in db.get_all_available_dentists()]
        msg = 'ok'
        _dict = {
            'message': msg,
            'dentists': _list
        }
        resp = make_response(jsonify(_dict))
        return resp
