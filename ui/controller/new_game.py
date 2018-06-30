from core.entity.game import Game
from core.storage.storage import Storage
from ui.action.action import Action
from ui.controller.base import Base
from ui.view.new_game import view as ng_view


class NewGame(Base):
    def __init__(self):
        super(NewGame, self).__init__(ng_view)

    def update(self, action: Action):
        if action is Action.INITIALIZE_GAME:
            game = Game()
            game.teams_count = int(self.view.ids['slider_count'].value)
            game.round_duration = self.view.ids['slider_dur'].value
            game.rounds_count = self.view.ids['slider_rounds'].value

            Storage.set('game', game)

            self.parent.next('team_setup', Action.EMPTY)
