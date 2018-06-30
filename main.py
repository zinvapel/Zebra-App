# -*- coding: UTF-8 -*-

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from ui.manager import Manager


class CrocoApp(App):
    manager = None

    def build(self):
        root_view = FloatLayout()
        self.manager = Manager(root_view)

        return root_view


if __name__ in ('__android__', '__main__'):
    CrocoApp().run()

