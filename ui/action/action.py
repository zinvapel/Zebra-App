import enum


class Action(enum.Enum):
    EMPTY = 'empty'

    INITIALIZE_GAME = 'initialize_game'

    # Team setting up actions
    TS_VALIDATE = 'ts_validate'
    TS_PREV = 'ts_prev'
    TS_NEXT = 'ts_next'
    TS_FINAL = 'ts_final'

    # Round actions
    SKIP = 'skip'
    ACCEPT = 'accept'

    # Round result actions
    REMOVE = 'remove'
    ADD = 'add'
    NEXT_ROUND = 'next_round'
