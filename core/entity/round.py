import enum


class RoundState(enum.Enum):
    INIT = 'init'
    READY = 'ready'
    IN_PROGRESS = 'in_progress'
    PLAYED = 'played'

    def is_ready(self):
        return self == self.READY


class Round:
    def __init__(self):
        self.number = 0
        self.level = None
        self.state = RoundState.INIT
        self.start_time = None
        self.duration = 0

        self.items = []
