class AbstractHardware(object):
    state = None
    name = None

    def __init__(self, name='undefined', state=0):
        self.name = name
        self.state = state

    def setup(self):
        pass

    def cleanup(self):
        pass

    def read_state(self):
        return self.state

    def write_state(self, state):
        self.state = state

        return self.state
