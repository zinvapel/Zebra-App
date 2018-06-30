view = """
#: import Action ui.action.action.Action

GridLayout:
    rows:2
    Label:
        text: "Help"
    Button:
        size_hint: 1, .2
        text: "Go back"
        on_press: app.manager.next('main', Action.EMPTY)
"""