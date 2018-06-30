view = """
#: import Action ui.action.action.Action

GridLayout:
    cols: 3
    slider_count: slider_count
    slider_dur: slider_dur
    slider_rounds: slider_rounds
    text_count: text_count
    text_dur: text_dur
    text_rounds: text_rounds
    GridLayout:
        cols: 1
        size_hint: .4, 1
        Label:
            text: "Количество команд"
        Label:
            text: "Продолжительность раунда"
        Label:
            text: "Количество раундов"
        Label:
            text: "Сложность"
        FloatLayout:
    GridLayout:
        cols: 1
        Slider:
            id: slider_count
            min: 2
            max: 4
            step: 1
            on_value: text_count.text = str(self.value)
        Slider:
            id: slider_dur
            min: 3
            max: 180
            step: 15
            on_value: text_dur.text = str(self.value)
        Slider:
            id: slider_rounds
            min: 1
            max: 5
            step: 1
            on_value: text_rounds.text = str(self.value)
        GridLayout:
            cols: 1
            Label:
                text: "Сложность пока не доступна"
        Button:
            text: "Next"
            on_press: app.manager.active().update(Action.INITIALIZE_GAME)
    GridLayout:
        cols: 1
        size_hint: .2, 1
        Label:
            id: text_count
            text: str(slider_count.value)
        Label:
            id: text_dur
            text: str(slider_dur.value)
        Label:
            id: text_rounds
            text: str(slider_rounds.value)
        Label:
            text: '@TODO'
        FloatLayout:
"""