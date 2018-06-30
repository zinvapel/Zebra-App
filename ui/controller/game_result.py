from kivy.properties import Logger

from core.storage.storage import Storage
from helper.round import RoundHelper
from ui.action.action import Action
from ui.controller.base import Base
from ui.view.game_result import view


class GameResult(Base):
    def __init__(self):
        super(GameResult, self).__init__(view)

    def update(self, action: Action):
        Logger.info("Update in RoundResult with action {action}".format(action=action))
        if action is Action.EMPTY:

            game = Storage.get('game')

            scores = {}
            for team in game.teams.values():
                self.view.ids.command_win.text = team.name
                scores[team.number] = RoundHelper.get_scores_for_team(game, team)
