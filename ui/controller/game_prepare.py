from kivy.app import App

from core.entity.round import RoundState
from core.storage.storage import Storage
from helper.round import RoundHelper
from ui.action.action import Action
from ui.controller.base import Base
from ui.view.game_prepare import view as gp_view


class GamePrepare(Base):
    def __init__(self):
        super(GamePrepare, self).__init__(gp_view)

    def update(self, action: Action):
        with Storage.update('game') as game:
            round_ = RoundHelper.get_one(game)
            if round_ is None:
                self.view.clear_widgets()  # @TODO REMOVE?
                App.get_running_app().manager.next('game_result_prepare', Action.EMPTY)
                return
            round_.state = RoundState.READY
            team = game.teams[RoundHelper.get_team_number(round_)]
            player = team.players[RoundHelper.get_player_number(round_)]

        self.view.ids['team_name'].text = str(team.name)
        self.view.ids['team_points'].text = str(RoundHelper.get_scores_for_team(game, team))
        self.view.ids['player_name'].text = str(player.name)
        self.view.ids['describer'].text = str(team.players["1" if player.id == "2" else "2"].name)


