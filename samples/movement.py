from blessed import Terminal
from entities import Entity

term = Terminal()


dir_map = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0)
}


def keyboard_movement(entity: Entity, direction: str, steps: int) -> None:
    """Handles player movement"""
    p, q = dir_map[direction]
    a, b = p * steps, q * steps
    entity.move_by(a, b)


def random_movement(entity: Entity) -> None:
    """Random npc movement"""
    pass
