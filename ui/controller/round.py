import time
import math

from kivy.app import App
from kivy.properties import Logger, Clock

from core.entity.round import RoundState
from core.storage.storage import Storage
from helper.round import RoundHelper
from source.sqlite.words import Words
from ui.action.action import Action
from ui.controller.base import Base
from ui.view.round import view


class Round(Base):
    current_points = 0
    schedule = None

    def __init__(self):
        super(Round, self).__init__(view)

        self.source = Words()

    def update(self, action: Action):
        Logger.info("Update in RoundController with action {action}".format(action=action))
        if action is Action.EMPTY:
            with Storage.update('game') as game:
                round_ = RoundHelper.get_ready(game)
                round_.state = RoundState.IN_PROGRESS
                round_.start_time = time.time()  # Start round

            self.start_clock()
            self.render_new()
            return

        if action is Action.SKIP:
            with Storage.update('game') as game:
                val = self.view.ids.val.val
                identifier = self.view.ids.identifier.val
                word_name = self.view.ids.word.text
                round_ = RoundHelper.get_active_round(game)
                round_.items.append(
                    {
                        "identifier": identifier,
                        "word": word_name,
                        "val": val,
                        "val_received": 0
                    }
                )
            self.render_new(list(map(lambda item: item['identifier'], round_.items)))
            return

        if action is Action.ACCEPT:
            with Storage.update('game') as game:
                val = self.view.ids.val.val
                identifier = self.view.ids.identifier.val
                word_name = self.view.ids.word.text
                round_ = RoundHelper.get_active_round(game)
                round_.items.append(
                    {
                        "identifier": identifier,
                        "word": word_name,
                        "val": val,
                        "val_received": val
                    }
                )
            self.render_new(list(map(lambda item: item['identifier'], round_.items)))
            return

        Logger.error(
            "Action {action} is not implemented in controller {controller}"
                .format(action=action, controller=self)
        )
        raise NotImplemented

    def render_new(self, previous_ids=None):
        if previous_ids is None:
            previous_ids = []
        word = self.source.get_not(previous_ids)
        self.view.ids.word.text = word['word']
        self.view.ids.val.val = word['value']
        self.view.ids.identifier.val = word['id']

    def start_clock(self):
        with Storage.update('game') as game:
            round_ = RoundHelper.get_active_round(game)
        self.view.ids.timer.ids.time.text = str(round_.duration)

        Round.schedule = Clock.schedule_interval(self.timer_update, 0.01)

    def timer_update(self, *largs):
        if self.view is None:
            return

        with Storage.update('game') as game:
            round_ = RoundHelper.get_active_round(game)
            if (time.time() - round_.start_time) >= round_.duration:
                self.finish()
                return

            self.view.ids.timer.angle = (360 / round_.duration) * (time.time() - round_.start_time)
            self.view.ids.timer.ids.time.text = str(round_.duration - math.floor(time.time() - round_.start_time))

    def finish(self):
        Clock.unschedule(Round.schedule)
        App.get_running_app().manager.next('round_result', Action.EMPTY)