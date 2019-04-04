# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.dentists import Dentists
from .api.dentists_id import DentistsId
from .api.dentists_id_timeslots import DentistsIdTimeslots


routes = [
    dict(resource=Dentists, urls=['/dentists'], endpoint='dentists'),
    dict(resource=DentistsId, urls=['/dentists/<int:id>'], endpoint='dentists_id'),
    dict(resource=DentistsIdTimeslots, urls=['/dentists/<int:id>/timeslots'], endpoint='dentists_id_timeslots'),
]