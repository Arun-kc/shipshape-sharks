from blessed import Terminal
from blocks import Blocks
from components.rectangle import Rectangle
from entities import Player
from movement import keyboard_movement
from perlin_map import PerlinMap

term = Terminal()

w, h = term.width, term.height - 1
speed = .1
key_to_dir_map = {
    term.KEY_UP: 'UP',
    term.KEY_DOWN: 'DOWN',
    term.KEY_LEFT: 'LEFT',
    term.KEY_RIGHT: 'RIGHT'
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
    print(term.home, end='')

    with term.cbreak(), term.hidden_cursor():
        inp = ''
        while inp.lower() != 'q':
            with term.location():
                print(term.move_xy(0, h), term.clear_eol, end='')
                print(term.move_xy(0, h), player.cur_tile, player.cur, end='')
                print(term.move_xy(60, h), player.lst_tile, player.lst, end='')

            inp = term.inkey(timeout=speed)

            if inp.code in key_to_dir_map:
                direction = key_to_dir_map[inp.code]
                keyboard_movement(player, direction, 1)

                with term.location():

                    # Prints player to updated positions
                    print(*player.affected_blocks, sep='', end='')
                    print(player, end='')

                    # Updates affected blocks of Map
                    # print(*player.affected_blocks, sep='', end='')

        print(term.clear)

# for i in range(10):
#     for j in range(10):
#         player.move_xy(i, j)
#         print(term.move_xy(0, 30), player.lst, player.lst_tile, end='', )
#         print(term.move_xy(115, 30), player.cur, player.cur_tile, end='')


if __name__ == '__main__':
    main()
