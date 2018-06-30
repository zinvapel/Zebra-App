view = """
#: import Action ui.action.action.Action

GridLayout:
    rows: 4
    Label:
        text: "End of round"
    GridLayout:
        cols: 2
        Label:
            id: word_total
            text: "Итого слов"
        Label:
            id: points_total
            text: "Итого очков"
    GridLayout:
        cols: 6
        id: words
    Button:
        text: "Next round"
        on_press: app.manager.active().update(Action.NEXT_ROUND)
"""
