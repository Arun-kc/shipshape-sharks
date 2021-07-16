from blessed import Terminal
from blocks import Blocks
from components.rectangle import Rectangle
from entities import Player
from movement import keyboard_movement
from perlin_map import PerlinMap

term = Terminal()

w, h = term.width, term.height - 1
steps = 1
speed = .01
key_dir_map = {
    term.KEY_UP: (0, -steps),
    term.KEY_DOWN: (0, steps),
    term.KEY_LEFT: (-steps, 0),
    term.KEY_RIGHT: (steps, 0)
}

game_map = PerlinMap(w, h, seed=50)
game_map.generate_map(Blocks)
map_matrix = game_map.MAP_matrix

player = Player('█', color='blue')
player.use_map(map_matrix, (0, 0), Rectangle(0, 0, w, h))


def main() -> None:
    """Main"""
    print(term.home + term.clear, end='')
    print(game_map, end='')
    print(player, end='')

    with term.cbreak(), term.hidden_cursor():
        inp = ''
        while str(inp).lower() != 'q':  # inp may be a tuple of keys' sequence or empty
            with term.location():
                print(term.move_xy(0, 31), term.clear_eol, end='')
                print(term.move_xy(0, 31), player.cur_tile, player.cur, end='')
                print(term.move_xy(50, 31), player.lst_tile, player.lst, end='')
                print(term.move_xy(100,31),player.lst_tile, "Press 'q' to Exit!", end='')

            inp = term.inkey(timeout=speed)

            if inp.code in key_dir_map:  # a movement command is given
                a, b = key_dir_map[inp.code]
                keyboard_movement(player, a, b)
                print(player, end='')
    print(term.clear)
# for i in range(10):
#     for j in range(10):
#         player.move_xy(i, j)
#         print(term.move_xy(0, 30), player.lst, player.lst_tile, end='', )
#         print(term.move_xy(115, 30), player.cur, player.cur_tile, end='')


if __name__ == '__main__':
    main()
