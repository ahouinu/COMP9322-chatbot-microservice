from __future__ import absolute_import

from pprint import pprint
from pymongo import MongoClient, ReturnDocument

client = MongoClient('localhost', 27017)
db = client['timeslots']
collection = db['collection']


def __get_a_timeslot(query: dict):
    '''
    get a timeslot document from collection
    :param query: a query dict
    :return: query result as a dict
    '''
    return collection.find_one(query)


def __get_timeslots(query: dict):
    '''
    get all timeslot documents satisfying the given query
    :param query: a query dict
    :return: an iteratable Cursor instance
    '''
    return collection.find(query)


def get_timeslot_by_datetime(date: str, time: str, doctor_id: int):
    return __get_a_timeslot({'date': date, 'time': time, 'doctor_id': doctor_id})


def get_all_available_timeslots():
    return __get_timeslots({'status': 'available'})


def get_all_available_timeslots_givin_doctor(doctor_id: int):
    return __get_timeslots({'status': 'available', 'doctor_id': doctor_id})


def update_timeslot(query: dict, update: dict, **kwargs):
    return collection.find_one_and_replace(query, update, **kwargs, return_document=ReturnDocument.AFTER)


# if __name__ == '__main__':
    # pprint(collection.find_one())
    # pprint(get_timeslot_by_datetime('Monday', '9'))
    # for _ in get_all_available_timeslots():
    #     pprint(_)
    # for _ in get_all_available_timeslots_givin_doctor(1):
    #     pprint(_)
    # pprint(update_timeslot({'date': 'Monday', 'time': '9', 'doctor_id': 0}, {'status': 'reserved'}))
