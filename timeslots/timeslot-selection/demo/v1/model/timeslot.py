from __future__ import absolute_import

from copy import deepcopy

from . import mongo_driver as db
from . import timeslot_exceptions as te

_weeksdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
_times = [str(_) for _ in range(9, 17)]
_status = ['reserved', 'available', 'rest']


class Timeslot:

    def __init__(self, _id: int, doctor_id: int, date: str, time: str, status: str = 'available', comments='',
                 reserved_by=''):

        self._id = _id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.status = status
        self.comments = comments
        self.reserved_by = reserved_by

        if date not in _weeksdays or time not in _times or status not in _status:
            raise te.ParameterError('bad parameters!')

    def check_availability(self):
        return self.status == 'available'

    def reserve(self, patient):
        if not self.check_availability():
            raise te.AvailabilityError('Timeslot not available')
        else:
            self.status = 'reserved'
            self.reserved_by = patient
            db.update_timeslot(self.mongo_view(ignore=['status', 'reserved_by']), self.mongo_view())

    def cancel(self, patient):
        if self.check_availability():
            raise te.AvailabilityError('Timeslot is not reserved by any patient, can not cancel')
        elif self.reserved_by != patient:
            raise te.AccessError('Only the creator can cancel this booking')
        else:
            self.status = 'available'
            self.reserved_by = ''
            db.update_timeslot(self.mongo_view(ignore=['status', 'reserved_by']), self.mongo_view())

    def mongo_view(self, ignore: list = None):
        _dict = deepcopy(self.__dict__)
        if ignore:
            for _ in ignore:
                _dict.pop(_)
        return _dict
