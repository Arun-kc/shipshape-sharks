import random

from blessed import Terminal
from blocks import Block
from components.rectangle import Perception, Rectangle

term = Terminal()


class Entity(Block):
    """Entity"""

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

    def __str__(self):
        return term.move_xy(*self.cur) + self._string

    def use_map(self, game_map: str, spawn: tuple, map_rect: Rectangle = None) -> None:
        """Init the map for entity"""
        x, y = spawn
        self.map = game_map

        self.cur = spawn
        self.lst = spawn

        self.lst_tile = self.map[y][x]
        self.cur_tile = self.map[y][x]

        self.map_rect = map_rect
        self.perc_square = Perception(spawn, self.perc_range)

        # Map Blocks Affected By Entity
        self.affected_blocks = []

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

        # Places player on nxt tile in map
        self.map[y][x] = self

        # Reset last map tile to it's actual value which is in self.lst_tile
        self.map[ly][lx] = self.lst_tile

        # Adds Last block to affected blocks for reprinting
        self.affected_blocks = [term.move_yx(ly, lx) + self.lst_tile]

    def _check_next_move(self, x: int, y: int) -> bool:

        if not self.map_rect.isContainingPoint((x, y)):
            return False

        nxt_tile = self.map[y][x]

        if getattr(nxt_tile, 'is_passable', None) is not None and not nxt_tile.is_passable:
            return False

        if term.strip(str(nxt_tile)) in self.unpassable_blocks:
            return False

        return True


class Player(Entity):
    """Player"""

    def set_stats(self, name: str = 'John', health_points: int = 500, attack_points: int = 25) -> None:
        """Set Player Stats"""
        self.name = name
        self.health_points = health_points
        self.attack_points = attack_points


class Mob(Entity):
    """Mob"""

    def set_stats(self) -> None:
        """Set Stats"""
        self.name = random.choice(['Thug', 'Bandit', 'Theif'])
        self.health_points = random.randrange(100, 200)
        self.attack_points = random.randrange(5, 10)
