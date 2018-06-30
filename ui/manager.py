from kivy.event import EventDispatcher
from kivy.properties import Logger
from kivy.uix.widget import Widget

from ui.action.action import Action
from ui.controller.base import Base
from ui.controller.game_prepare import GamePrepare
from ui.controller.game_result import GameResult
from ui.controller.new_game import NewGame
from ui.controller.records import Records
from ui.controller.round import Round
from ui.controller.round_result import RoundResult
from ui.controller.team_setup import TeamSetUp
from ui.view.main import view as main_view
from ui.view.help import view as help_view
from ui.view.game_result_prepare import view as game_result_prepare_view


class Manager(EventDispatcher):
    this = None

    def __init__(self, root_view: Widget):
        Manager.this = self

        self.root_view = root_view
        self.controller_list = {
            'main': Base(main_view),
            'records': Records(),
            'help': Base(help_view),
            'new_game': NewGame(),
            'team_setup': TeamSetUp(),
            'game_prepare': GamePrepare(),
            'round': Round(),
            'round_result': RoundResult(),
            'game_result_prepare': Base(game_result_prepare_view),
            'game_result': GameResult()
        }
        self.active_controller = None
        self.next('main', Action.EMPTY)

    def active(self):
        return self.active_controller

    def next(self, key: str, action: Action):
        Logger.info("Redirecting to controller '{key}'".format(key=key))

        if key not in list(self.controller_list.keys()):
            Logger.error("Unknown controller '{key}'".format(key=key))
            raise NotImplemented # @TODO ERROR HANDLING

        self.active_controller = self.controller_list[key]
        self.change_active_controller(action)

    def change_active_controller(self, action):
        # Hide current layout
        self.root_view.clear_widgets() # @TODO ANIMATION
        # Render new current layout
        self.root_view.add_widget(self.active().execute(action).view)
