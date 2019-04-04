# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from pprint import pprint

from flask import g, make_response, jsonify, request

from . import Resource
from ..model import mongo_driver as db


class Timeslots(Resource):

    def get(self):
        pprint(request.args)
        doc_id = request.args.get('doc_id', None)
        user_selected_day = request.args.get('user_selected_day', None)
        user_selected_time = request.args.get('user_selected_time', None)

        if user_selected_day and user_selected_time:
            return self.check_availability(user_selected_day, user_selected_time, doc_id)
        else:
            return self.get_by_id(doc_id)

    @staticmethod
    def get_by_id(doc_id):
        # pprint(g.args)
        try:
            doctor_id = int(doc_id)
        except KeyError:
            return {'message': f'Can not find the dentist on server with doc_id={doctor_id}'}, 400, None
        _list = [_ for _ in db.get_all_available_timeslots_givin_doctor(doctor_id)]
        msg = 'OK'
        _dict = {
            'message': msg,
            'timeslots': _list
        }
        resp = make_response(jsonify(_dict), 200)
        return resp

    @staticmethod
    def check_availability(day, time, doc_id):
        result = db.get_timeslot_by_datetime(day, time, int(doc_id))
        _list = [result]
        msg = 'OK'
        _dict = {
            'message': msg,
            'timeslots': _list
        }
        resp = make_response(jsonify(_dict), 200)
        return resp
