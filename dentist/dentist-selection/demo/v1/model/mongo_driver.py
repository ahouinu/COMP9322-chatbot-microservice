from __future__ import absolute_import

import os
from pprint import pprint
from pymongo import MongoClient, ReturnDocument

# client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
client = MongoClient('localhost', 27017)
db = client['dentists']
collection = db['collection']


def __get_a_dentist(query: dict):
    '''
    get a dentist document from collection
    :param query: a query dict
    :return: query result as a dict
    '''
    return collection.find_one(query)


def __get_dentists(query: dict):
    '''
    get all dentist documents satisfying the given query
    :param query: a query dict
    :return: an iteratable Cursor instance
    '''
    return collection.find(query)


def get_dentist_by_id(id: int):
    return __get_a_dentist({'_id': id})


def get_dentist_by_datetime(date: str, time: str, doctor_id: int):
    return __get_a_dentist({'date': date, 'time': time, 'doctor_id': doctor_id})


def get_all_available_dentists():
    return __get_dentists({})


def update_dentist(query: dict, update: dict, **kwargs):
    return collection.find_one_and_replace(query, update, **kwargs, return_document=ReturnDocument.AFTER)


# if __name__ == '__main__':
#     pprint(collection.find_one())
#     pprint(get_dentist_by_datetime('Monday', '9'))
#     for _ in get_all_available_dentists():
#         pprint(_)
#     for _ in get_all_available_dentists_givin_doctor(1):
#         pprint(_)
#     pprint(update_dentist({'date': 'Monday', 'time': '9', 'doctor_id': 0}, {'status': 'reserved'}))
