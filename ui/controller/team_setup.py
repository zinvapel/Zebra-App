from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle

from core.entity.game import Game
from core.entity.team import Team
from core.storage.storage import Storage
from ui.action.action import Action
from ui.controller.base import Base
from ui.view.team_setup import view as team_setup_view


class TeamSetUp(Base):
    def __init__(self):
        super(TeamSetUp, self).__init__(team_setup_view)

        self.made = []
        self.last_updated = 0

    def update(self, action: Action):
        if action is Action.TS_PREV:
            print("Render prev") # TODO ADD
        elif action is Action.TS_NEXT:
            self.create_next()
        elif action is Action.TS_FINAL:
            self.create_next()
            with Storage.update('game') as game:
                game.configure_rounds()
            self.parent.next('game_prepare', Action.EMPTY)
        # Just render

    def validate(self, id):
        with self.view.ids[id].canvas.after:
            if self.view.ids[id].text != '':
                Color(0, 1, 0, 1)
            else:
                Color(1, 0, 0, 1)

    def create_next(self): # @TODO ADD VALIDATION
        with Storage.update('game') as game:
            team = Team(self.last_updated)
            if team.number not in self.made:
                self.made.append(team.number)
                team.name = self.view.ids['tname'].text
                team.players["1"].name = self.view.ids['p1name'].text
                team.players["2"].name = self.view.ids['p2name'].text
                game.teams[str(self.last_updated)] = team
                self.last_updated += 1

        self.render_next(game)

    def render_next(self, game: Game):
        self.view.ids['tname'].text = ''
        self.view.ids['p1name'].text = ''
        self.view.ids['p2name'].text = ''

        if game.teams_count - len(game.teams) == 1:
            self.view.ids['next_btn'].action = Action.TS_FINAL
