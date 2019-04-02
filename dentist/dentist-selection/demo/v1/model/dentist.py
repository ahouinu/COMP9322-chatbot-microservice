_valid_specs = [
    'Paediatric Dentistry',
    'Orthodontics',
    'Oral Surgery'
]


class Dentist:

    def __init__(self, _id, name, location, specialization):
        assert(specialization in _valid_specs)
        self._id = _id
        self.name = name
        self.location = location
