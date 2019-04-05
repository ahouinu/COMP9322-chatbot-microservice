from __future__ import absolute_import

from pprint import pprint
from random import randint

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
    AVAILABLE_PROB = 40
    counter = 1
    if not collection.find_one():   # do not double init
        for doctor_id in range(0, 3):
            for w in _weeksdays:
                for t in _times:
                    # set status with probability
                    p = randint(0, 100)
                    if p > AVAILABLE_PROB:
                        status = 'reserved'
                        reserved_by = 'SYSTEM'
                        comments = 'This timeslot is locked by admin'
                    else:
                        status = 'available'
                        reserved_by, comments = '', ''
                    timeslot = Timeslot(counter, doctor_id, w, t,
                                        status=status, reserved_by=reserved_by, comments=comments)
                    insert_timeslot(timeslot)
                    pprint(f'Inserting...{timeslot.mongo_view()}')
                    counter += 1


if __name__ == '__main__':
    init_db()
