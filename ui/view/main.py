view = """
#: import Action ui.action.action.Action

GridLayout:
    rows:3
    Label:
        text: "Крокодил"
    FloatLayout:
        Button:
            text: "Новая игра"
            size_hint: .8, .2
            pos_hint: { 'center_x': .5, 'y': .7 }
            color: 0, 0, 0, 1
            background_color: 1, 1, 1, 0 
            pressed_color: .6, .6, .6, 1 
            normal_color: .8, .8, .8, 1 
            bg_color: .8, .8, .8, 1 
            on_touch_down: self.bg_color = self.pressed_color if self.collide_point(*args[1].pos) else self.bg_color
            on_touch_up: self.bg_color = self.normal_color if self.collide_point(*args[1].pos) else self.bg_color
            on_press: app.manager.next('new_game', Action.EMPTY)
            canvas.before:
                Color:
                    rgba: self.bg_color
                RoundedRectangle:
                    size: self.size 
                    pos: self.pos
                    radius: (self.size[1]/2, self.size[1]/2)
        Button:
            text: "Рекорды"
            size_hint: .8, .2
            pos_hint: { 'center_x': .5, 'y': .4 }
            color: 0, 0, 0, 1
            background_color: 1, 1, 1, 0 
            pressed_color: .6, .6, .6, 1 
            normal_color: .8, .8, .8, 1 
            bg_color: .8, .8, .8, 1 
            on_touch_down: self.bg_color = self.pressed_color if self.collide_point(*args[1].pos) else self.bg_color
            on_touch_up: self.bg_color = self.normal_color if self.collide_point(*args[1].pos) else self.bg_color
            on_press: app.manager.next('records', Action.EMPTY)
            canvas.before:
                Color:
                    rgba: self.bg_color
                RoundedRectangle:
                    size: self.size 
                    pos: self.pos
                    radius: (self.size[1]/2, self.size[1]/2)
        Button:
            text: "Как играть"
            size_hint: .8, .2
            pos_hint: { 'center_x': .5, 'y': .1 }
            color: 0, 0, 0, 1
            background_color: 1, 1, 1, 0 
            pressed_color: .6, .6, .6, 1 
            normal_color: .8, .8, .8, 1 
            bg_color: .8, .8, .8, 1 
            on_touch_down: self.bg_color = self.pressed_color if self.collide_point(*args[1].pos) else self.bg_color
            on_touch_up: self.bg_color = self.normal_color if self.collide_point(*args[1].pos) else self.bg_color
            on_press: app.manager.next('help', Action.EMPTY)
            canvas.before:
                Color:
                    rgba: self.bg_color
                RoundedRectangle:
                    size: self.size 
                    pos: self.pos
                    radius: (self.size[1]/2, self.size[1]/2)
"""
# @TODO move to main styles
