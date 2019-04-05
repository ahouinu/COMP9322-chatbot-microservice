import os
from collections import defaultdict
from pprint import pprint
from typing import List

import requests
from flask import Flask, make_response, jsonify, request
from .jwt_encoder import encode_user_id

app = Flask(__name__)
TIMESLOT_URL = os.environ['TIMESLOT_URL']
DENTIST_URL = os.environ['DENTIST_URL']


def textify(msg: str) -> dict:
    return {'text': msg}


def get_dentists():
    return requests.get(f'{DENTIST_URL}/v1/dentists')


def get_timeslots(doc_id):
    return requests.get(f'{DENTIST_URL}/v1/dentists/{doc_id}/timeslots')


def check_availability(doc_id, day, time):
    return requests.get(
        f'{TIMESLOT_URL}/v1/timeslots?doc_id={doc_id}&user_selected_day={day}&user_selected_time={time}')


def reserve_timeslot(user_id, doc_id, timeslot_id):
    token = encode_user_id(user_id)
    headers = {'Authorization': token}
    return requests.put(f'{TIMESLOT_URL}/v1/timeslots/{timeslot_id}/reserve?doc_id={doc_id}', headers=headers)


def cancel_timeslot(user_id, doc_id, timeslot_id):
    token = encode_user_id(user_id)
    headers = {'Authorization': token}
    return requests.put(f'{TIMESLOT_URL}/v1/timeslots/{timeslot_id}/cancel?doc_id={doc_id}', headers=headers)


@app.route('/chat', methods=['POST'])
def handle_message():
    pprint(request.form)
    user_id = request.form.get('chatfuel user id')
    messages = []
    reply = {'text': 'Test Reply!'}
    messages.append(reply)
    resp = make_response(jsonify(messages))

    return resp


@app.route('/chat', methods=['GET'])
def return_message():
    pprint(request.args)
    args = request.args.to_dict()
    pprint(args)
    user_id, action = request.args.get('chatfuel user id', None), \
                      request.args.get('action', None)
    messages: List[dict] = []
    payload = {}

    if action == 'get_dentists':
        dentists = get_dentists().json()['dentists']
        set_attrs = {}
        for d in dentists:
            msg = f'Doctor {d["_id"] + 1}: {d["name"]}\n' \
                f'Location: {d["location"]}\n' \
                f'Specialization: {d["specialization"]}'
            messages.append(textify(msg))
            set_attrs[f'doc_name_{d["_id"] + 1}'] = d["name"]
        payload = {
            'set_attributes': set_attrs,
            'messages': messages
        }

    elif action == 'get_timeslots':
        doc_id = request.args.get('doc_id', None)
        timeslots = get_timeslots(doc_id).json()['timeslots']
        timeslots_dict_by_day = defaultdict(list)
        _weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for t in timeslots:
            _id = t['_id']
            day = t['date']
            time = t['time']
            msg = f'No. {_id} at {time}:00'
            timeslots_dict_by_day[day].append(msg)
        for day in sorted(timeslots_dict_by_day.keys(), key=_weekday_order.index):
            day_msg = f'{day}: \n'
            for m in timeslots_dict_by_day[day]:
                day_msg += f'{m}\n'
            messages.append(textify(day_msg))
        payload = {'messages': messages}

    elif action == 'check_availability':
        doc_id = request.args.get('doc_id', None)
        day = request.args.get('user_selected_day', None)
        time = request.args.get('user_selected_time', None)

        timeslot = check_availability(doc_id, day, time).json()['timeslots'][0]
        set_attrs = {}
        day = timeslot['date']
        time = timeslot['time']
        if timeslot['status'] == 'available':
            msg = f'The timeslot you asked at {time}:00 on {day} is available!'
            messages.append(textify(msg))
            # set_attrs['availability'] = 'yes'
            set_attrs['timeslot_id'] = timeslot['_id']
            redirect_list = ['Book Timeslots API Call']
            payload = {
                'set_attributes': set_attrs,
                'messages': messages,
                'redirect_to_blocks': redirect_list
            }
        else:
            msg = f'I\'m sorry, but the timeslot you asked at {time}:00 on {day} is already reserved.\n'
            messages.append(textify(msg))
            # set_attrs['availability'] = 'no'
            redirect_list = ['Alternative Timeslots']
            payload = {
                'messages': messages,
                'redirect_to_blocks': redirect_list
            }

    elif action == 'reserve_timeslot':
        doc_id = request.args.get('doc_id', None)
        timeslot_id = request.args.get('timeslot_id', None)
        resp = reserve_timeslot(user_id, doc_id, timeslot_id)
        pprint(resp.json())

        if resp.status_code == 200:
            messages.append(textify('Your reservation has been accomplished!'))
            set_attrs = {}
            timeslot = resp.json()['timeslot']
            set_attrs['timeslot_day'] = timeslot['date']
            set_attrs['timeslot_time'] = timeslot['time']
            dentists = get_dentists().json()['dentists']
            my_dentist = dentists[int(doc_id) - 1]
            set_attrs['doc_location'] = my_dentist['location']
            set_attrs['doc_spec'] = my_dentist['specialization']
            payload = {
                'messages': messages,
                'set_attributes': set_attrs,
                'redirect_to_blocks': ['Confirmation']
            }

        else:
            messages.append(textify('Something went wrong... I\'m sorry about that'))
            redirect_list = ["Welcome Message", "Default Answer"]
            payload = {
                'messages': messages,
                'redirect_to_blocks': redirect_list
            }

    elif action == 'cancel_timeslot':
        doc_id = request.args.get('doc_id', None)
        timeslot_id = request.args.get('timeslot_id', None)

        resp = cancel_timeslot(user_id, doc_id, timeslot_id)
        pprint(resp.json())

        if resp.status_code == 200:
            messages.append(textify('Your previous booking has been cancelled!'))
            payload = {
                'messages': messages,
            }

        else:
            messages.append(textify('Something went wrong... I\'m sorry about that'))
            redirect_list = ["Welcome Message", "Default Answer"]
            payload = {
                'messages': messages,
                'redirect_to_blocks': redirect_list
            }

    pprint(payload)
    resp = make_response(jsonify(payload))
    return resp
