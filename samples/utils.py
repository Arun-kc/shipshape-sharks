from blessed import Terminal

term = Terminal()


class Panel:
    """Creates customized Rectangles"""

    def __init__(
        self,
        string: str,
        size: tuple = None,
        padding: int = 1,
        offset: tuple = None,
        color: str = '',
        align: str = 'ljust'
    ):
        ox, oy = offset or term.get_location()
        width, height = size or (None, None)
        color = getattr(term, color, None)
        align = getattr(term, align, term.ljust)

        mx_width = width - padding * 2 if width else self._find_default_width(string)

        row_format = f'{ term.move_x( ox ) }{ " " * padding }{ {} }{ " " * padding }{ term.move_down }'
        empty_row = row_format.format(' ' * mx_width)

        rows = string.strip()
        rows = term.wrap(rows, width=mx_width)

        rows = [row_format.format(align(row, mx_width)) for row in rows]
        rows = [empty_row] * padding + rows + [empty_row] * padding

        self._string = term.move_y(oy) + (''.join(rows))

        if color:
            self._string = color(self._string)

    def __str__(self):
        return self._string

    def __repr__(self):
        return repr(self._string)

    def _find_default_width(self, string: str) -> int:
        return max(map(len, string.split('\n')))
