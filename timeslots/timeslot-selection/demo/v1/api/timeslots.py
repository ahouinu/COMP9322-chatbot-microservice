# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from pprint import pprint

from flask import g, make_response, jsonify

from . import Resource
from ..model import mongo_driver as db


class Timeslots(Resource):

    def get(self):
        pprint(g.args)
        try:
            doctor_id = g.args['doc_id']
        except KeyError:
            return {'message': f'Can not find the dentist on server with doc_id={doctor_id}'}, 400, None
        _list = [_ for _ in db.get_all_available_timeslots_givin_doctor(doctor_id)]
        msg = 'OK'
        _dict = {
            'message': msg,
            'timeslots': _list
        }
        resp = make_response(jsonify(_dict))
        return resp
