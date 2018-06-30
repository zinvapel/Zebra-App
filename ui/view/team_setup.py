from kivy.uix.textinput import TextInput

view = """
#: import Action ui.action.action.Action

GridLayout:
    cols: 2
    GridLayout:
        cols: 2
        GridLayout:
            cols: 1
            Label:
                text: "Имя команды"
            Label:
                text: "Игрок 1"
            Label:
                text: "Игрок 2"
            FloatLayout:
        GridLayout:
            cols: 1
            TextInput:
                id: tname
                on_text_validate: app.manager.active().validate
            TextInput:
                id: p1name
                on_text_validate: app.manager.active().validate
            TextInput:
                id: p2name
                on_text_validate: app.manager.active().validate
            FloatLayout:
    GridLayout:
        cols: 2
        GridLayout:
            cols: 1
            Label:
                text: "Цвет команды"
            FloatLayout:
            FloatLayout:
            FloatLayout:
        GridLayout:
            cols: 1
            Label:
                id: color
                text: "@TODO"
            FloatLayout:
            FloatLayout:
            Button:
                id: next_btn
                action: Action.TS_NEXT
                text: "Next"
                on_press: app.manager.active().update(self.action)
"""
TextInput
