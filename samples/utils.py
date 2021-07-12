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
        align: str = 'center',
        valign: str = 'center'
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

        rows = [row_format.format(align(row, mx_width)[:mx_width]) for row in rows]

        mx_height = height - padding * 2 if height else len(rows)

        extra_top_pad = extra_bottom_pad = 0
        if mx_height > len(rows):
            diff = mx_height - len(rows)
            extra_top_pad, extra_bottom_pad = self._find_extra_pad(diff, valign)

        total_top_pad, total_bottom_pad = padding + extra_top_pad, padding + extra_bottom_pad
        rows = [empty_row] * total_top_pad + rows[:mx_height] + [empty_row] * total_bottom_pad

        self._string = term.move_y(oy) + (''.join(rows))

        if color:
            self._string = color(self._string)

    def __str__(self):
        return self._string

    def __repr__(self):
        return repr(self._string)

    def __add__(self, string: str):
        return self._string + str(string)

    def _find_default_width(self, string: str) -> int:
        return max(map(len, string.split('\n')))

    def _find_extra_pad(self, diff: int, valign: str) -> tuple:

        if valign == 'top':
            return 0, diff
        elif valign == 'bottom':
            return diff, 0
        else:
            return diff // 2 + diff % 2, diff // 2


if __name__ == '__main__':
    print(
        term.home+term.clear,
        Panel('', size=(4, 4), offset=(100, 25), color='on_green'),
        Panel('', size=(2, 2), offset=(101, 26), color='on_blue')
    )
