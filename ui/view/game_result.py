view = """
#: import Action ui.action.action.Action

GridLayout:
    cols: 1
    rows: 3
    Label:
        id: command_win
        text: "None"
    Label:
        id: best
        text: "None"
    GridLayout:
        cols: 2
        RoundedButton:
            text: "Retry"
        RoundedButton:
            text: "Main menu"
            on_press: app.manager.next('main', Action.EMPTY)
"""

