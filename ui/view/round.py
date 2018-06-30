view = """
#: import Action ui.action.action.Action

FloatLayout:
    GridLayout:
        rows: 3
        Label:
            id: word
            text: "WORD"
            size_hint: 1, .7
        GridLayout:
            cols: 2
            size_hint: 1, .3
            Button:
                text: "Skip"
                on_press: app.manager.active().update(Action.SKIP)
            Button:
                text: "Accept"
                on_press: app.manager.active().update(Action.ACCEPT)
    Hidden:
        id: val
    Hidden:
        id: identifier
    RoundedTimer:
        id: timer
        size_hint: .1, None
        y: self.x
        pos_hint: {'right': .95, 'top': .8}
"""
