# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g, make_response, jsonify

from . import Resource
from .. import schemas
from ..model import mongo_driver as db
from ..model import Timeslot
from ..model.timeslot_exceptions import *


class TimeslotsIdCancel(Resource):

    def put(self, id):
        print(g.headers)
        print(g.args)

        try:
            token = g.headers['Authorization']
            doctor_id = g.args['doc_id']
        except KeyError:
            return {'message': 'missing parameters'}, 400, None

        _ts = db.get_timeslot_by_id(id, doctor_id)
        if _ts:
            timeslot = Timeslot(**_ts)
            try:
                timeslot.cancel(token)
            except (AvailabilityError, AccessError)as e:
                return {'message': f'{str(e)}'}, 400, None
            msg = 'Cancelled successfully'
            _dict = {
                'message': msg,
                'timeslot': timeslot.mongo_view()
            }
            resp = make_response(jsonify(_dict))
            return resp
        else:
            return {'message': 'Timeslot Not Found'}, 404, None
