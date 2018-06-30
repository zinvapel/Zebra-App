from kivy.app import App
from kivy.properties import Logger

from core.entity.round import RoundState
from core.storage.storage import Storage
from helper.round import RoundHelper
from ui.action.action import Action
from ui.controller.base import Base
from ui.view.round_result import view
from widget.button import WordButton


class RoundResult(Base):
    def __init__(self):
        super(RoundResult, self).__init__(view)

    def update(self, action: Action):
        Logger.info("Update in RoundResult with action {action}".format(action=action))
        if action is Action.EMPTY:
            game = Storage.get('game')
            round_ = RoundHelper.get_active_round(game)
            for item in round_.items:
                self.create_button(item)
            return

        if action is Action.REMOVE:
            with Storage.update('game') as game:
                pass
            return

        if action is Action.ADD:
            with Storage.update('game') as game:
                pass
            return

        if action is Action.NEXT_ROUND:
            with Storage.update('game') as game:
                round_ = RoundHelper.get_active_round(game)
                for result in self.view.ids.words.children:
                    for item in round_.items:
                        if item['identifier'] == result.idx:
                            item['val_received'] = item['val'] if result.is_active else 0
                self.clear()
                RoundHelper.get_active_round(game).state = RoundState.PLAYED
                App.get_running_app().manager.next('game_prepare', Action.EMPTY)
            return

        Logger.error(
            "Action {action} is not implemented in controller {controller}"
                .format(action=action, controller=self)
        )
        raise NotImplemented

    def create_button(self, item):
        btn = WordButton(
            txt=item['word'],
            is_active=item['val_received'] == item['val']
        )

        btn.idx = item['identifier']
        btn.btn.bind(on_press=RoundResult.change_word_state)
        self.view.ids.words.add_widget(btn)

    def clear(self):
        self.view.ids.words.clear_widgets()

    @staticmethod
    def change_word_state(btn):
        btn.container.is_active = not btn.container.is_active
