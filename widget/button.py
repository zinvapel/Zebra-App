from kivy.graphics.vertex_instructions import Line
from kivy.properties import BooleanProperty
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


class WordButton(RelativeLayout):
    is_active = BooleanProperty(None)

    def __init__(self, txt, is_active, **kwargs):
        super(WordButton, self).__init__(**kwargs)

        self.btn = Button(text=txt)
        self.idx = None
        self.line = None
        self.btn.container = self

        with self.btn.canvas.after:
            self.line = Line(width=20)
            self.btn.bind(size=self._resize, pos=self._resize)

        self.is_active = is_active
        self.add_widget(self.btn)

    def _resize(self, *args, **kwargs):
        if not self.is_active:
            self.line.points = [
                0 + self.btn.width * 1/8, self.btn.height / 2,
                self.btn.width * 7/8, self.btn.height / 2
            ]

    def on_is_active(self, btn, is_active):
        if is_active:
            self.line.points = []
        else:
            self._resize()

