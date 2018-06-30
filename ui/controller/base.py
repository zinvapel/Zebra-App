from kivy.lang import Builder
from kivy.properties import Logger

from ui.action.action import Action


class Base:
    def __init__(self, view: str):
        self.__view_string = view
        self.view = None

        import ui.manager
        self.parent = ui.manager.Manager.this

    # final #
    def execute(self, action: Action):
        if self.view is None:
            Logger.info("Trying to load view in {controller}".format(controller=self))
            self.view = Builder.load_string(self.__view_string)

        self.update(action)

        return self

    def update(self, action: Action):
        Logger.info("Update with {action} is not defined in {controller}".format(controller=self, action=action))

