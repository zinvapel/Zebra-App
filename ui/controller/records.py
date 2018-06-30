from kivy.properties import Logger

from ui.action.action import Action
from ui.controller.base import Base
from ui.view.records import view as records_view
from source.sqlite.records import Records as RecordsSource


class Records(Base):
    def __init__(self):
        super(Records, self).__init__(records_view)

        self.source = RecordsSource()

    def update(self, action: Action):
        records = self.get_records()
        Logger.info(repr(records))
        for index in range(0, 5):
            score = getattr(self.view.ids['rec_grid'], 'rec_s_' + str(index + 1))

            if index < len(records):
                score.ids['score'].text = str(records[index]['score'])
                score.ids['name'].text = str(records[index]['player'])
            else:
                score.ids['score'].text = '---'
                score.ids['name'].text = '---'

    def get_records(self):
        return self.source.get()