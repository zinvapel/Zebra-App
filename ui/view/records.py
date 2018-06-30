view = """
#: import Action ui.action.action.Action

GridLayout:
    rows:2
    Label:
        text: "Records"
        size_hint: 1, .2
    GridLayout:
        id: rec_grid
        rec_s_1: rec_s_1.__self__
        rec_s_2: rec_s_2.__self__
        rec_s_3: rec_s_3.__self__
        rec_s_4: rec_s_4.__self__
        rec_s_5: rec_s_5.__self__
        rows: 6
        size_hint: 1, .9
        Score:
            id: rec_s_1
        Score:
            id: rec_s_2
        Score:
            id: rec_s_3
        Score:
            id: rec_s_4
        Score:
            id: rec_s_5
        Button:
            text: "Go back"
            on_press: app.manager.next('main', Action.EMPTY)
            size_hint: 1, .16
"""