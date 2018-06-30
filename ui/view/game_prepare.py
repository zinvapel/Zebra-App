view = """
#: import Action ui.action.action.Action

GridLayout:
    cols: 1
    GridLayout:
        cols: 2
        size_hint: 1, .5
        GridLayout:
            cols: 1
            Label:
                text: "Team"
            Label:
                text: "Total points"
            Label:
                text: "Player in check"
        GridLayout:
            cols: 1
            Label:
                id: team_name
                text: "NAME"
            Label:
                id: team_points
                text: "123"
            Label:
                id: player_name
                text: "NAME OF PLAYER"
    GridLayout:
        cols: 1
        size_hint: 1, .25
        Label:
            id: describer
            text: "Give computer to player NAME"
    GridLayout:
        cols: 1
        size_hint: 1, .25
        Button:
            text: "Start"
            on_press: app.manager.next('round', Action.EMPTY)
"""

