from kivy.properties import Logger

from core.entity.round import Round


class Game:
    def __init__(self):
        self.teams_count = 0
        self.teams = {}

        self.round_duration = 0
        self.rounds_count = 0
        self.rounds = {}

    def configure_rounds(self):
        for r_number in range(0, self.rounds_count):
            for t_number, team in self.teams.items():
                for p_number in "12":
                    round_ = Round()
                    round_.duration = self.round_duration
                    round_.number = '{rounds}_{teams}_{players}'.format(rounds=r_number, teams=t_number, players=p_number)
                    self.rounds[round_.number] = round_

        Logger.info("Game configured")
        Logger.info("   Rounds: {c}".format(c=len(self.rounds)))
        Logger.info("   Teams: {c}".format(c=len(self.teams)))