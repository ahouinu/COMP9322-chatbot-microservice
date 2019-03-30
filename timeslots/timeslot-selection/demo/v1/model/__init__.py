from __future__ import absolute_import

from pprint import pprint

from .mongo_driver import collection
from .timeslot import Timeslot, _weeksdays, _times


def insert_timeslot(timeslot: Timeslot):
    '''
    Inserts a Timeslot into mongodb collection as a document
    :param timeslot: a Timeslot instance
    :return: None
    '''
    collection.insert_one(timeslot.mongo_view())


def init_db():
    counter = 1
    if not collection.find_one():   # do not double init
        for doctor_id in range(0, 3):
            for w in _weeksdays:
                for t in _times:
                    timeslot = Timeslot(counter, doctor_id, w, t)
                    insert_timeslot(timeslot)
                    pprint(f'Inserting...{timeslot.mongo_view()}')
                    counter += 1


if __name__ == '__main__':
    init_db()
