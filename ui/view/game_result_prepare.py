view = """
#: import Action ui.action.action.Action

GridLayout:
    cols: 1
    rows: 2
    Label:
        text: "Game over"
    RoundedButton:
        text: "View results"
        on_press: app.manager.next('game_result', Action.EMPTY)
"""

