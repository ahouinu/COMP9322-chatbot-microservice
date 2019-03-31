

class ParameterError(Exception):

    def __init__(self, msg):
        self.msg = msg


class AvailabilityError(Exception):

    def __init__(self, msg):
        self.msg = msg


class AccessError(Exception):

    def __init__(self, msg):
        self.msg = msg

