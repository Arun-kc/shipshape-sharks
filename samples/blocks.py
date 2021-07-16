from blessed import Terminal

term = Terminal()


class Block:
    """Block"""

    def __init__(self, spirite: str, color: str = None, bg_color: str = None):
        self.spirite = spirite
        self._string = spirite

        if color:
            self.color = getattr(term, color)
            self._string = self.color(self._string)

        if bg_color:
            self.bg_color = getattr(term, bg_color)
            self._string = self.bg_color(self._string)

    def __str__(self):
        return self._string

    def __add__(self, string: str):
        return str(self) + str(string)

    def __radd__(self, string: str):
        return str(string) + str(self)


class Earth(Block):
    """Earth Block"""

    is_passable = True
    settings = {
        "profiles": {
            "normal": {
                "noise_value": -25,
                "spirite_options": {
                    " ": 0,
                    # '▓': -5,
                },
                "color_options": {
                    None: 0,
                },
                "bg_color_options": {
                    'on_chartreuse': 0,
                    'on_chartreuse2': -7,
                    'on_chartreuse3': -15,
                },
            },
            "desert": {
                "noise_value": -30,
                "spirite_options": {
                    " ": 0,
                },
                "color_options": {
                    None: 0,
                },
                "bg_color_options": {
                    'on_gold1': -10,
                    'on_gold2': -15,
                },
            }
        }
    }


class Water(Block):
    """Water Entity"""

    is_passable = False
    settings = {
        "profiles": {
            "normal": {
                "noise_value": -100,
                "spirite_options": {
                    " ": 0,
                },
                "color_options": {
                    None: 0,
                },
                "bg_color_options": {
                    # term.on_steelblue: 10,
                    # term.on_steelblue2: -6,
                    'on_steelblue3': 0,
                },
            },
            "desert": {
                "noise_value": -100,
                "spirite_options": {
                    " ": 0,
                },
                "color_options": {
                    None: 0,
                },
                "bg_color_options": {
                    # term.on_steelblue: 10,
                    # term.on_steelblue2: -6,
                    'on_steelblue1': 0,
                },
            }
        }
    }


Blocks = [Earth, Water]
