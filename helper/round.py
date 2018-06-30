from core.entity.game import Game
from core.entity.round import RoundState, Round
from core.entity.team import Team


class RoundHelper:
    @staticmethod
    def get_first(game: Game):
        return game.rounds["0_0_1"]

    @staticmethod
    def get_one(game: Game):
        for round_ in game.rounds.values():
            if round_.state == RoundState.INIT:
                return round_

        return None

    # @TODO add get_next
    # @staticmethod
    # def get_next(game: Game):
    #     pass

    @staticmethod
    def get_ready(game: Game):
        for round_ in game.rounds.values():
            if round_.state == RoundState.READY:
                return round_

    @staticmethod
    def get_active_round(game: Game):
        for round_ in game.rounds.values():
            if round_.state == RoundState.IN_PROGRESS:
                return round_

    @staticmethod
    def get_real_number(round_: Round):
        return round_.number[:1]

    @staticmethod
    def get_team_number(round_: Round):
        return round_.number[2:3]

    @staticmethod
    def get_player_number(round_: Round):
        return round_.number[4:5]

    @staticmethod
    def get_scores_for_team(game: Game, team: Team):
        scores = 0
        for round_ in game.rounds.values():
            if RoundHelper.get_team_number(round_) == team.number:
                scores += round_.score

        return scores
