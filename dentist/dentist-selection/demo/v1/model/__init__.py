from __future__ import absolute_import

from pprint import pprint

from .mongo_driver import collection
from .dentist import Dentist, _valid_specs


def insert_dentist(dentist: Dentist):
    '''
    Inserts a Dentist into mongodb collection as a document
    :param dentist: a Dentist instance
    :return: None
    '''
    collection.insert_one(dentist.__dict__)


def init_db():
    fake_names = ['Dr. Shawn', 'Dr. Miller', 'Dr. Eric']
    fake_locations = ['K17-B08 Drum', 'K17-G07 Bongo', 'J17-302a Viola']
    if not collection.find_one():
        for doctor_id, doctor_name, location, spec in \
                zip(range(0, 3), fake_names, fake_locations, _valid_specs):
            dentist = Dentist(doctor_id, doctor_name, location, spec)
            insert_dentist(dentist)
            pprint(f'Inserting...{dentist.__dict__}')


if __name__ == '__main__':
    pprint(f'Connecting to db collection: {collection}')
    init_db()
