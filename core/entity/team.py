from core.entity.player import Player


class Team:
    def __init__(self, number: int):
        self.number = number
        self.name = None
        self.color = None

        self.players = {
            "1": Player(1),
            "2": Player(2)
        }
