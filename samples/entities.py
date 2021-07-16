import random

from blessed import Terminal

from components.rectangle import Perception, Rectangle
from objects import Block

term = Terminal()


class Entity(Block):
    """Player"""

    # representing set map blocks which are not passable
    unpassable_blocks = {}

    def __init__(
        self,
        spirite: str,
        color: str = None,
        bg_color: str = None,
        is_passable: bool = False,
        perc_range: int = 1
    ):
        super().__init__(spirite, color=color, bg_color=bg_color)
        self.is_passable = is_passable
        self.perc_range = perc_range

    def use_map(self, game_map: str, spawn: tuple, map_rect: Rectangle = None) -> None:
        """Init the map for entity"""
        x, y = spawn
        self.map = game_map

        self.cur = spawn
        self.lst = spawn
        self._str = term.move_xy(x, y) + self.color(self.spirite)
        self.lst_tile = self.map[y][x]
        self.cur_tile = self.map[y][x]

        self.map_rect = map_rect
        self.perc_square = Perception(spawn, self.perc_range)

    def move_by(self, a: int, b: int) -> None:
        """Move Player To new Place"""
        lx, ly = self.cur
        x, y = lx + a, ly + b

        if not self._check_next_move(x, y):
            return

        self.lst = self.cur
        self.cur = x, y
        self.lst_tile = self.cur_tile
        self.cur_tile = self.map[y][x]
        self.map[y][x] = self
        self.map[ly][lx] = self.lst_tile

        with term.location():
            self._str = term.move_yx(ly, lx) + self.lst_tile + term.move_xy(x, y) + self.color(self.spirite)


    def _check_next_move(self, x: int, y: int) -> bool:

        if not self.map_rect.isContainingPoint((x, y)):
            return False

        nxt_tile = self.map[y][x]

        if getattr(nxt_tile, 'is_passable', None) and not nxt_tile.is_passable:
            return False

        if term.strip(str(nxt_tile)) in self.unpassable_blocks:
            return False

        return True


class Player(Entity):
    """Player"""

    def __init__(self, name: str = 'John', health_points: int = 500, attack_points: int = 25):
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points

    def init_entity(
        self,
        spirite: str,
        color: str = None,
        bg_color: str = None,
        is_passable: bool = False,
        perc_range: int = 1
    ) -> None:
        """Init Super class"""
        super().__init__(spirite, color, bg_color, is_passable, perc_range)


class Mob(Entity):
    """Mob"""

    def __init__(self):
        self.name = random.choice(['Thug', 'Bandit', 'Theif'])
        self.health_points = random.randrange(100, 200)
        self.attack_points = random.randrange(5, 10)

    def init_entity(self, color: str, spirite: str, is_passable: bool) -> None:
        """Init Super class"""
        super().__init__(self, color, spirite, is_passable)
